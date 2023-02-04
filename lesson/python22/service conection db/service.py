import sqlite3

class Client:

    def __init__(self, nick='', password='', conn=None, addr=None):
        self._nick = nick
        self._password = password
        self._conn = conn
        self._addr = addr

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

class ServiceToConectionDatabase(object):

    __DB_LOCATION = 'clients.db'

    def connection(self):
        connection = None
        try:
            connection = sqlite3.connect(ServiceToConectionDatabase.__DB_LOCATION)
            print("Connection to MySQL DB successful")
            return connection
        except sqlite3.Error as e:
            print(f'Error connecting to sqlite: {e}')
        # finally:
        #     if connection:
        #         connection.close()
        #         print('SQLite connection closed')

    def insert(self, name_table, columns_table, variables):
        mydb = self.connection()
        mycursor = mydb.cursor()
        sql = "INSERT INTO {0} ({1}) VALUES {2}".format(name_table, columns_table,[ [c.nick, c.password, c.conn, c.addr] for c in variables])
        mycursor.execute(sql)
        mydb.commit()

        print(mycursor.rowcount, "record inserted.")

    def select(self, name_table):
        mydb = self.connection()
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM {0}".format(name_table))
        myresult = mycursor.fetchall()

        print(myresult)

    def select_where(self, name_table, column, value):
        mydb = self.connection()
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM {0} WHERE {1} = '{2}'".format(name_table, column, value))
        myresult = mycursor.fetchall()

        print(myresult)
        return myresult

    def delete(self, name_table, columns_table, variables):
        mydb = self.connection()
        mycursor = mydb.cursor()
        sql = "DELETE FROM {0} WHERE {1} = '{2}'".format(name_table, columns_table, variables)
        mycursor.execute(sql)
        mydb.commit()
        print(mycursor.rowcount, "record(s) deleted")

    def update(self, name_table, columns_table, first_variable, second_variable):
        mydb = self.connection()
        mycursor = mydb.cursor()
        sql = "UPDATE {0} SET {1} = '{3}' WHERE {1} = '{2}'".format(name_table, columns_table,
                                                                    first_variable, second_variable)
        mycursor.execute(sql)
        mydb.commit()
        print(mycursor.rowcount, "record(s) affected")

db = ServiceToConectionDatabase()
# val = ['mery', '123', 1, 1]
val = Client('mery', '123')
db.insert('clients', 'nick, password, conn, addr', val)

# c1.insert(name_table,columns_table,variables)
# for x in c1.select(name_table):
#     print(x)

# c1.delete(name_table,columns_table,variables)

# c1.update(name_table,columns_table,variables1,variables2)
# for x in c1.select(name_table):
#     print(x)

# name_table = ("nbu")
# column = 'cc'
# value = 'USD'
#
# c1 = db()
# j = c1.select_where(name_table,column,value)
# print(j[0][3])
# # for x in j:
# #     print(x)
# #     print(x[3])
