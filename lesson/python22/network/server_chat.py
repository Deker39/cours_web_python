import socket
import threading
import time


class Client:
    items = []

    def __init__(self, nick='', password='', conn=None, addr=None):
        self._nick = nick
        self._password = password
        self._conn = conn
        self._addr = addr
        Client.items.append(self)

    def __str__(self):
        return f'Nick:{self._nick}, Pass:{self._password},' \
               f' conn: {self._conn}, addr:{self.addr}'

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

    @property
    def conn(self):
        return self._conn

    @conn.setter
    def conn(self, value):
        self._conn = value

    @conn.deleter
    def conn(self):
        del self._conn

    @property
    def addr(self):
        return self._addr

    @addr.setter
    def addr(self, value):
        self._addr= value

    @addr.deleter
    def addr(self):
        del self._addr


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
    print(f"User {nick} ")
    broadcast(f"{nick} connected!".encode('utf-8'))
    conn.send('You connected to server!'.encode('utf-8'))
    time.sleep(1)
    conn.send('OK'.encode('utf-8'))
    [print(i) for i in list_Clients]
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

