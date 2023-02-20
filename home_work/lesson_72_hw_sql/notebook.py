from mysql.connector import connect, Error

CREATE_DB = 'CREATE DATABASE IF NOT EXISTS`notebook`;'
CREATE_TABLE_NOTE = 'CREATE table note(' \
                   'id int auto_increment primary key,' \
                   'notes varchar(255),' \
                   'user_id int,' \
                   'date_creat datetime,' \
                    'foreign key (user_id) references user(id));'

CREATE_TABLE_USER = 'CREATE table user(' \
                    'id int auto_increment primary key,' \
                    'login varchar(255) not null,' \
                    'password varchar(255)not null,' \
                    'user_name varchar(255));'

USER_COL = ['login', 'password', 'user_name']
NOTE_COL = ['notes', 'date_creat']


def insert(c, table, col, val):
    c.execute(f'INSERT INTO {table} ({", ".join(col)}) VALUES ({val})')

k = ['alexx', '123', 'alex']

print(', '.join(['\''+i+'\'' for i in k]))

try:
    with connect(
        host='localhost',
        user='root',
        password='26091998@Asd',
        database='notebook'
    ) as conn:
        with conn.cursor() as cur:
            insert(cur, 'user', USER_COL, ', '.join(['"'+i+'"' for i in k]))
            conn.commit()




except Error as e:
    print(e)