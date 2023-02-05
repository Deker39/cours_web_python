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
        self._addr = value

    @addr.deleter
    def addr(self):
        del self._addr
