import socket
import threading
import time
from connect import ServiceToConnectionDatabase
from sample import Client


sock = socket.socket()
HOST = '127.0.0.1'
PORT = 9999
sock.bind((HOST, PORT))
sock.listen()
clients = []
nicknames = ['alex']
passwords = ['123']
list_Clients = [Client('alex', '123'), Client('din', '111')]
# c = Client()
db = ServiceToConnectionDatabase()


def check_pass(nick, password):
    return True if password == ''.join([i.password for i in list_Clients if i.nick == nick]) else False


def broadcast(message):
    for client in list_Clients:
        if client.conn is not None:
            client.conn.send(message)


def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = [i for i in list_Clients if i.conn == client]
            list_Clients.remove(index[0])
            broadcast(f'{index[0].nick} out!'.encode('utf-8'))
            client.close()
            break


def connect_client(conn, nick):
    list_Clients.append(c) if nick not in [i.nick for i in list_Clients] else False
    db.insert(c)
    print(f"User {nick} ")
    broadcast(f"{nick} connected!".encode('utf-8'))
    conn.send('You connected to server!'.encode('utf-8'))
    time.sleep(1)
    conn.send('OK'.encode('utf-8'))
    # [print(i) for i in list_Clients]
    thread1 = threading.Thread(target=handle, args=(conn,))
    thread1.start()


def new_client(conn, nick):
    conn.send(f'Hello, {nick}, you new participant'.encode('utf-8'))
    connect_client(conn, nick)


def old_client(conn, nick):
    conn.send('Welcome'.encode('utf-8'))
    connect_client(conn, nick)


def check_client(nick, password, conn):
    if nick in [i.nick for i in list_Clients] and nick != '':

        if check_pass(nick, password):
            old_client(conn, nick)
        else:
            conn.send('Your password not correct, plc try again'.encode('utf-8'))
            conn.send('REPEATPASS'.encode('utf-8'))
            c.password = conn.recv(1024).decode('utf-8')

            if check_pass(nick, c.password):
                old_client(conn, nick)

    elif nick == '' or nick == ' ':
        conn.send('Your nickname is emptiness'.encode('utf-8'))
        conn.send('REPEATNICK'.encode('utf-8'))
        c.nick = conn.recv(1024).decode('utf-8')
        check_client(nick, password, conn)

    else:
        new_client(conn, nick)


def receive():
    global c
    while True:
        c = Client()
        c.conn, c.addr = sock.accept()
        print(f"Connect with {str(c.addr)}")
        c.conn.send('NICKNAME'.encode('utf-8'))
        c.nick, c.password = eval(c.conn.recv(1024).decode('utf-8'))
        if c.nick in [i.nick for i in list_Clients]:
            old_cl = [i for i in list_Clients if c.nick == i.nick]
            old_cl[0].conn, old_cl[0].addr = c.conn, c.addr
            c.conn, c.addr = old_cl[0].conn, old_cl[0].addr
            check_client(c.nick, c.password, c.conn)
        else:
            check_client(c.nick, c.password, c.conn)


receive()

