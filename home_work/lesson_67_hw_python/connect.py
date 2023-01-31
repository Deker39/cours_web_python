import sqlite3
# from server_chat import Client

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

def creat_teble_clients(cur):
    cur.execute('''CREATE TABLE clients
                        (id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nick TEXT,
                        password TEXT,
                        conn NULL,
                        addr NULL)
                     ''')


try:
    con = sqlite3.connect('clients.db')
    cursor = con.cursor()
    print('Connection was successful')

    cursor.execute('''SELECT name FROM sqlite_master WHERE type='table' AND name='clients' ''')
    if cursor.fetchone()[0]:
        print('Table exists')
        list_Clients = [Client('alex', '123'), Client('din', '111')]
        # TODO проверка пользователя, доваление каждого пользователя в базу, удаление пользователя, апдейт данных пользователя
        # FIXME not work
        [cursor.execute('''INSERT INTO clients (nick, password, conn, addr) VALUES (?, ?, ?, ?)''',
                        [c.nick, c.password, c.conn, c.addr]) for c in list_Clients]
        # TODO work
        for c in list_Clients:
            cursor.execute('''INSERT INTO clients (nick, password, conn, addr) VALUES (?, ?, ?, ?)''',
                           [c.nick, c.password, c.conn, c.addr])
        con.commit()

    else:
        print('Table not exists')
        print('Table create')
        creat_teble_clients(cursor)


except sqlite3.Error as e:
    print(f'Error connecting to sqlite: {e}')
finally:
    if con:
        con.close()
        print('SQLite connection closed')
