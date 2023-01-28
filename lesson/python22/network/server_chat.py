import socket
import threading
import time

sock = socket.socket()
HOST = '127.0.0.1'
PORT = 9999
sock.bind((HOST, PORT))
sock.listen()
clients = []
nicknames = ['alex']
passwords = ['123']
list_Clients = []


class Client:

    def __init__(self, nick='', password=''):
        self._nick = nick
        self._password = password

    @property
    def nick(self) -> str:
        return self._nick

    @nick.setter
    def nick(self, value):
        self._nick = value

    @nick.deleter
    def nick(self):
        del self._nick

    @property
    def password(self) -> str:
        return self._password

    @password.setter
    def password(self, value):
        self._password = value

    @password.deleter
    def password(self):
        del self._password


def check_pass(nick, password):
    return True if passwords[nicknames.index(nick)] == password else False


def broadcast(message):
    for client in clients:
        client.send(message)


def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f'{nickname} out!'.encode('utf-8'))
            nicknames.remove(nickname)
            break


def connect_client(conn, nick):
    nicknames.append(nick) if nick not in nicknames else False
    clients.append(conn)
    print(f"User {nick} ")
    broadcast(f"{nick} connected!\n".encode('utf-8'))
    conn.send('You connected to server!\n'.encode('utf-8'))
    thread1 = threading.Thread(target=handle, args=(conn,))
    thread1.start()


def new_client(conn, nick):
    conn.send(f'Hello, {nick}, you new participant'.encode('utf-8'))
    connect_client(conn, nick)


def old_client(conn, nick):
    conn.send('Welcome'.encode('utf-8'))
    connect_client(conn, nick)


def check_client(nick, password, conn):
    if nick in nicknames and nick != '':
        if check_pass(nick, password):
            old_client(conn, nick)
            # conn.send('Welcome'.encode('utf-8'))
            # connect_client(conn, nick)
        else:
            conn.send('Your password not correct, plc try again'.encode('utf-8'))
            conn.send('REPEATPASS'.encode('utf-8'))
            password = conn.recv(1024).decode('utf-8')
            if check_pass(nick, password):
                old_client(conn, nick)
                # conn.send('Welcome'.encode('utf-8'))
                # connect_client(conn, nick)

    elif nick == '' or nick == ' ':
        conn.send('Your nickname is emptiness'.encode('utf-8'))
        conn.send('REPEATNICK'.encode('utf-8'))
        nick = conn.recv(1024).decode('utf-8')
        check_client(nick, password, conn)

    else:
        new_client(conn, nick)
        # conn.send(f'Hello, {nick}, you new participant'.encode('utf-8'))
        # connect_client(conn, nick)


def receive():
    conn, addr = sock.accept()
    print(f"Connect with {str(addr)}")
    conn.send('NICKNAME'.encode('utf-8'))
    nick, password = eval(conn.recv(1024).decode('utf-8'))
    check_client(nick, password, conn)



receive()

