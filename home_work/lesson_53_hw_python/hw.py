import hashlib
import json
import os

ADMIN_FILE_DIRECTORY = 'admin_file'
USERS_FILE_DIRECTORY = 'users_file'
TESTS_FILE_DIRECTORY = 'tests_file'

class Person:

    def __init__(self,login,password):
        self._login = login
        self._password = password

    @property
    def login(self):
        return self._login

    @login.setter
    def login(self,value:str):
        self._login = str(hashlib.md5(value.encode('ascii')).digest())

    @login.deleter
    def login(self):
        del self._login

    @property
    def password(self):
        return  self._password

    @password.setter
    def password(self,value:str):
        self._password = str(hashlib.md5(value.encode('ascii')).digest())

    @password.deleter
    def password(self):
        del self._password


# class User(Person):
#
#     def __init__(self,login,password,first_name,last_name,address,tel):
#         super().__init__(login,password)
#         self.first_name = first_name
#         self.last_name = last_name
#         self.address = address
#         self.tel = tel
#
class Admin(Person):
    def __init__(self,login,password):
        super().__init__(login,password)



def loading_toJSON(value,directory):
    try:
        with open(f'{directory}.json','w') as write_file:
            json.dump(value,write_file)
    except  Exception as e:
        print(f'Error: {str(e)}')

def unloading_toJSON(directory):
    try:
        with open(f'{directory}.json', "r") as read_file:
            return json.load(read_file)
    except  Exception as e:
        print(f'Error: {str(e)}')




admin_data = unloading_toJSON(ADMIN_FILE_DIRECTORY)

print('who are you?\n1.User\n2.Admin\n3.Exit')
main_choice = int(input('Choose: '))

while main_choice != 3:
    if main_choice == 1:
        #TODO Зделать запрос  файл с пользоватлями и проверить логин на уникальность, если нету то на
        # регистрацию, если есть то дальше по скрипту вести
        pass
    if main_choice == 2:
        if not os.path.isfile(f'{ADMIN_FILE_DIRECTORY}.json') or admin_data == None or 'password' not in admin_data or 'login' not in admin_data:
            admin = Admin('', '')
            print('it\'s you first entrance')
            admin.login = input('please write login: ')
            admin.password = input('please write password: ')
            loading_toJSON({'login': admin.login, 'password':admin.password}, ADMIN_FILE_DIRECTORY)
        else:

            #TODO 'admin has already been created
            print('Pleace, enter login and password')
            l,p = [hashlib.md5(input('Enter login: ').encode('ascii')).digest(),
                   hashlib.md5(input('Enter password: ').encode('ascii')).digest()]
            if admin_data['login'] == str(l) and admin_data['password'] == str(p):

                print('Welcom admin')
                print('1.Сhange login details\n2.User management\n3.View statistics\n4.Test management\n5.Return to menu above')
                admin_choise = int(input('Choose: '))
                while admin_choise != 5:
                    if admin_choise == 1:
                        pass
                    if admin_choise == 2:
                        pass
                    if admin_choise == 3:
                        pass
                    if admin_choise == 4:
                        pass

                    admin_choise = int(input('Choose: '))
            else:
                print('Incorrect login or password')

    main_choice = int(input('Choose: '))

