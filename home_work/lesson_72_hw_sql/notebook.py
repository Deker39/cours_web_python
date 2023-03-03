from connector import *
import datetime

CREATE_TABLE_NOTE = 'CREATE table note(' \
                    'id int auto_increment primary key,' \
                    'name_note varchar(255),' \
                    'note varchar(255),' \
                    'user_id int,' \
                    'date_creat date,' \
                    'data_edit date,' \
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


def output_notes(user_name, notes):
    time_format = "%d-%m-%Y"
    print(f'Name: {user_name}')
    [print(f'{note[0]}:\n'
           f'\t{note[1]}\n'
           f'created: {note[2].strftime(time_format)}\n',
           f'edited: {note[3].strftime(time_format)}\n' if note[2] != note[3] else ''
           ) for note in notes]


def add_note(db, login):
    name_note = input('Enter name note: ')
    note = input('Enter note: ')
    date_now = datetime.datetime.now().strftime("%Y-%d-%m")
    db.insert('notebook.note', NOTE_COLUMNS, "'{}', '{}', '{}', '{}', '{}'".
              format(name_note, note, db.select('notebook.user', 'id', f'login = "{login}"')[0][0], date_now, date_now))
    print('Entry added')


def del_note(db, login):
    name_note = input('Enter name note: ')
    id_user = db.select('notebook.user', 'id', f'login = "{login}"')[0][0]
    db.delete('notebook.note', f'name_note = "{name_note}" AND user_id = {id_user}')
    print('note to delete')


def edit_note(db, login):
    date_now = datetime.datetime.now().strftime("%Y-%d-%m")
    name_note = input('Enter name note: ')
    id_user = db.select('notebook.user', 'id', f'login = "{login}"')[0][0]
    old_note = db.select('notebook.note', 'notes', f'user_id = {id_user} and name_note = "{name_note}"')
    print(f'Content:\n\t{old_note[0][0]}')
    new_note = input('Enter new note: ')
    db.update('notebook.note', f'notes = "{new_note}", data_edit = "{date_now}"', f'user_id = {id_user} and name_note = "{name_note}"')
    print('note updated')


def show_note(db, login):
    id_user = db.select('notebook.user', 'id', f'login = "{login}"')[0][0]
    user_name = db.select('notebook.user', 'user_name', f'login = "{login}"')[0][0]
    notes = db.select('notebook.note', 'name_note, notes, date_creat, data_edit', f'user_id = {id_user}')
    output_notes(user_name, notes)


def show_note_time(db, login):
    user_name = db.select('notebook.user', 'user_name', f'login = "{login}"')[0][0]
    print('Enter the start date of the period')
    day_f, month_f, year_f = input('Enter a day: '), input('Enter a month: '), input('Enter a year: ')
    print('Now enter the end date of the period')
    day_t, month_t, year_t = input('Enter a day: '), input('Enter a month: '), input('Enter a year: ')
    notes = db.select('notebook.note',
                      'name_note, notes, date_creat, data_edit',
                      f'date_creat between "{"-".join([year_f, day_f,month_f])}" and "{"-".join([year_t, day_t, month_t])}" '
                      f'or data_edit between "{"-".join([year_f, day_f,month_f])}" and "{"-".join([year_t, day_t, month_t])}"')
    output_notes(user_name, notes)


def show_note_key_words(db, login):
    id_user = db.select('notebook.user', 'id', f'login = "{login}"')[0][0]
    user_name = db.select('notebook.user', 'user_name', f'login = "{login}"')[0][0]
    key_words = input('Enter keywords through "," : ')
    l = ''
    for i in key_words.split(","):
        l += f'notes like "{i.lstrip().rstrip()}" or '

    notes = db.select('notebook.note',
                      'name_note, notes, date_creat, data_edit',
                      f'user_id = {id_user} and {l.rstrip("or ")}')
    output_notes(user_name, notes)



def authorization(db):
    # TODO test value
    # login, password, nickname = 'alex', '123', 'deker'
    login = input('Please enter your login: ')
    if not check_login(db, login):
        print('you are new user')
        password = input('Please enter your password: ')
        nickname = input('Please enter your nickname: ')
        db.insert('notebook.user', USER_COLUMNS, "'{}', '{}', '{}'".format(login, password, nickname))
        print('your account added to database')
        # TODO прописать сюда цыклю программы а то только создает пользователя и выходит

    else:
        # password = '123'
        password = input('Please enter your password: ')

        while not check_pass(db, password):
            print('yor pass not correct')
            password = input('Please enter your password: ')

        choose = menu()

        while choose != 7:

            if choose == 1:
                add_note(db, login)
                choose = menu()
            elif choose == 2:
                del_note(db, login)
                choose = menu()
            elif choose == 3:
                edit_note(db, login)
                choose = menu()
            elif choose == 4:
                show_note(db, login)
                choose = menu()
            elif choose == 5:
                show_note_time(db, login)
                choose = menu()
            elif choose == 6:
                show_note_key_words(db, login)
                choose = menu()
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
