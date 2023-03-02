from connector import *
import datetime

CREATE_TABLE_NOTE = 'CREATE table note(' \
                    'id int auto_increment primary key,' \
                    'name_note varchar(255),' \
                    'note varchar(255),' \
                    'user_id int,' \
                    'date_creat datetime,' \
                    'data_edit datetime,' \
                    'foreign key (user_id) references user(id));'

CREATE_TABLE_USER = 'CREATE table user(' \
                    'id int auto_increment primary key,' \
                    'login varchar(255) not null,' \
                    'password varchar(255)not null,' \
                    'user_name varchar(255));'

USER_COLUMNS = "login, password, user_name"
NOTE_COLUMNS = "name_note, notes, user_id, date_creat, data_edit"


def print_menu(func):
    def inner():
        print('\nWork with the note\n')
        print('1.Add note\n'
              '2.Delete note\n'
              '3.Edit note\n'
              '4.Show note\n'
              '5.Show note by date (from to)\n'
              '6.Show a note that contains keywords\n'
              '7.Exit\n')
        return func()

    return inner


@print_menu
def menu():
    return int(input('Choose: '))


def check_database(db, database_name):
    return True if db.fetchall(f'SHOW DATABASES LIKE "{database_name}"') else False


def check_table(db, table_name):
    return True if db.fetchall(f'SHOW TABLES FROM notebook LIKE "{table_name}"') else False


def check_login(db, login):
    return True if db.select('notebook.user', 'login', f'login = "{login}"') else False


def check_pass(db, password):
    return True if db.select('notebook.user', 'password', f'password = "{password}"') else False


def add_note(db, login):
    name_note = input('Enter name note: ')
    note = input('Enter note: ')
    db.insert('notebook.note', NOTE_COLUMNS, "'{}', '{}', '{}', '{}', '{}'".
              format(name_note, note, db.select('notebook.user', 'id', f'login = "{login}"')[0][0],
                     datetime.datetime.now().strftime("%d.%m.%Y"), datetime.datetime.now().strftime("%d.%m.%Y")))
    # TODO не выходит с функции
    print('Entry added')


def del_note():
    pass


def edit_note():
    pass


def show_note():
    pass


def show_note_time():
    pass


def show_note_key_words():
    pass


def authorization(db):
    # TODO test value
    login, password, nickname = 'alex', '123', 'deker'
    # login = input('Please enter your login: ')
    if not check_login(db, login):
        print('you are new user')
        # password = input('Please enter your password: ')
        # nickname = input('Please enter your nickname: ')
        db.insert('notebook.user', USER_COLUMNS, "'{}', '{}', '{}'".format(login, password, nickname))
        print('your account added to database')

    else:
        password = '123'
        password = input('Please enter your password: ')

        while not check_pass(db, password):
            print('yor pass not correct')
            password = input('Please enter your password: ')

        choose = menu()

        while choose != 7:

            if choose == 1:
                add_note(db, login)
            elif choose == 2:
                del_note()
            elif choose == 3:
                edit_note()
            elif choose == 4:
                show_note()
            elif choose == 5:
                show_note_time()
            elif choose == 6:
                show_note_key_words()
            else:
                print('Incorrect value')

    print('App closed')


def main():
    db = Database()

    if not check_database(db, 'notebook'):
        db.create_database('notebook')
        print('creat db')
    else:
        print('bd has been created')

    if not check_table(db, 'user'):
        db.create_table('notebook.user', 'id int auto_increment primary key,'
                                         ' login varchar(255) not null,'
                                         ' password varchar(255)not null,'
                                         'user_name varchar(255)')
        print('user table creat')
    else:
        print('user table has been created')

    if not check_table(db, 'note'):
        db.create_table('notebook.note', 'id int auto_increment primary key,'
                                         'name_note varchar(255),'
                                         'notes varchar(255),'
                                         'user_id int,'
                                         'date_creat datetime,'
                                         'data_edit datetime,'
                                         'foreign key (user_id) references user(id)')
        print('note table creat')
    else:
        print('note table has been created')

    authorization(db)


if __name__ == '__main__':
    main()
