import sqlite3
from sample import Client


class ServiceToConnectionDatabase:

    __DB_LOCATION = 'clients.db'

    def __init__(self):
        """Initialize db class variables"""
        self.__con = sqlite3.connect(ServiceToConnectionDatabase.__DB_LOCATION)
        self.cur = self.__con.cursor()

    def __del__(self):
        """close sqlite3 connection"""
        self.__con.close()

    def commit(self):
        """commit changes to database"""
        self.__con.commit()
        self.__del__()

    def create_table(self):
        self.cur.execute('''CREATE TABLE clients
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nick TEXT,
                            password TEXT,
                            conn INTEGER,
                            addr TEXT)
                         ''')

    def insert(self, value: Client):
        self.cur.execute('''INSERT INTO clients (nick, password, conn, addr) VALUES (?, ?, ?, ?)''',
                         (value.nick, value.password, value.conn.fileno(), str(value.addr)))
        self.commit()

    def update(self, value):
        self.cur.execute('''UPDATE clients SET nick = ?, password = ?, conn = ?, addr = ? WHERE nick = ?''', value)
        self.commit()

    def select(self):
        self.cur.execute('''SELECT * FROM clients''')
        return self.cur.fetchall()

    def select_where(self, value):
        self.cur.execute('''SELECT * FROM clients WHERE nick = ? ''', [value])
        return self.cur.fetchall()


# db = ServiceToConectionDatabase()
# kek = Client('miya','234', "<socket.socket fd=168, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 9999), raddr=('127.0.0.1', 50076)>", '127.0.0.1')
#
# db.insert([kek])
# db.commit()
# print(db.select_where
# (name))
# if db.select_where(name):
#     db.update([26, 9, name])
#     print('update')
#     db.commit()
