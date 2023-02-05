import sqlite3
from sample import Client


class ServiceToConnectionDatabase:

    __DB_LOCATION = 'clients.db'

    def __init__(self):
        """Initialize db class variables"""
        self._con = sqlite3.connect(ServiceToConnectionDatabase.__DB_LOCATION)
        self._con.row_factory = lambda cur, row: row[0]
        self.cur = self._con.cursor()

    def __del__(self):
        """close sqlite3 connection"""
        self._con.close()

    def commit(self):
        """commit changes to database"""
        self._con.commit()
        self.__del__()

    def create_table(self):
        self.cur.execute('''CREATE TABLE clients
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nick TEXT,
                            password TEXT,
                            conn TEXT,
                            addr TEXT)
                         ''')

    def check_table(self):
        return True if self.cur.execute('''SELECT name FROM sqlite_master WHERE type='table' AND name='clients' ''').fetchone()[0] else False

    def insert(self, value: Client):
        """INSERT INTO mysql_table (column1, column2, …) VALUES (value1, value2, …)"""
        self.cur.execute('''INSERT INTO clients (nick, password, conn, addr) VALUES (?, ?, ?, ?)''',
                         (value.nick, value.password, str(value.conn), str(value.addr)))
        self.commit()

    def update(self, tab_name, col, value, cond, cond_value):
        """UPDATE table_name SET column1 = value1, column2 = value2...., columnN = valueN WHERE [condition]"""
        self.cur.execute(f'UPDATE {tab_name} SET {",".join([f"""{c} = "{v}" """ for c, v in zip(col, value)])} WHERE {cond} = "{cond_value}"')
        self.commit()

    def select(self, col, tab_name):
        """SELECT column1, column2, columnN FROM table_name"""
        self.cur.execute(f'SELECT {col} FROM {tab_name}')
        return self.cur.fetchall()

    def select_where(self, col, tab_name, cond, cond_value):
        """SELECT column1, column2, columnN FROM table_name WHERE condition"""
        self.cur.execute(f'SELECT {col} FROM {tab_name} WHERE {cond} = "{cond_value}" ')
        return self.cur.fetchall()
