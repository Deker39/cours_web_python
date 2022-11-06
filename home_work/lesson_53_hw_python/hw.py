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

class User(Person):

    def __init__(self,login,password,first_name,last_name,address,tel,passed_test = list,pending_tests = list):
        super().__init__(login,password)
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.tel = tel
        self.passed_test = passed_test
        self.pending_tests= pending_tests

class Admin(Person):
    def __init__(self,login,password):
        super().__init__(login,password)

class Test:

    def __init__(self,section,exam_name,test_dict):
        self._section = section
        self._exam_name = exam_name
        self._test_dict = test_dict

    @property
    def section(self):
        return self._section

    @section.setter
    def section(self,value):
        self._section = value

    @section.deleter
    def section(self):
        del self._section

    @property
    def exam_name(self):
        return self._exam_name

    @exam_name.setter
    def exam_name(self, value):
        self._exam_name = value

    @exam_name.deleter
    def exam_name(self):
        del self._exam_name

    @property
    def test_dict(self):
        return self._test_dict

    @test_dict.setter
    def test_dict(self,value):
        self._test_dict = value

    @test_dict.deleter
    def test_dict(self):
        del self._test_dict

def loading_toJSON(value,directory):
    try:
        with open(f'{directory}.json','w') as write_file:
            json.dump(value,write_file, indent=4)
    except  Exception as e:
        print(f'Error: {str(e)}')

def unloading_toJSON(directory):
    try:
        with open(f'{directory}.json', "r") as read_file:
            return json.load(read_file)
    except  Exception as e:
        print(f'Error: {str(e)}')


admin_data = unloading_toJSON(ADMIN_FILE_DIRECTORY)
user_data  = unloading_toJSON(USERS_FILE_DIRECTORY)
test_data = unloading_toJSON(TESTS_FILE_DIRECTORY)


print('who are you?\n1.User\n2.Admin\n3.Exit')
main_choice = int(input('Choose: '))

while main_choice != 3:
    if main_choice == 1:
        if not os.path.isfile(f'{USERS_FILE_DIRECTORY}.json'):

            user = User('', '', '', '', '', '')
            print('Pleace, enter login and password')
            user.login = input('please write login: ')
            user.password = input('please write password: ')
            user.first_name = input('please write first name: ')
            user.last_name = input('please write last name: ')
            user.address = input('please write address: ')
            user.tel = input('please write tel: ')

            loading_toJSON({'1': {'login': user.login, 'password': user.password,
                                  'first_name': user.first_name,
                                  'last_name': user.last_name, 'address': user.address,
                                  'tel': user.tel, 'passed_test': user.passed_test, 'pending_tests': user.pending_tests}}
                           , USERS_FILE_DIRECTORY)
        else:
            user = User('', '', '', '', '', '')
            print('Pleace, enter login and password')
            user.login = input('please write login: ')
            user.password = input('please write password: ')
            check = [user_data[i]['login'] for i in user_data.keys()]
            if user.login in check:
                print('вы уже есть в системе ')
                print(check.index(user.login)+1)
                print(user_data[str(check.index(user.login)+1)].values())

            else:
                print('новый пользователь продолжыте решистрацию')
                user.first_name = input('please write first name: ')
                user.last_name = input('please write last name: ')
                user.address = input('please write address: ')
                user.tel = input('please write tel: ')
                user_data.update({len(user_data) + 1: {'login': user.login, 'password': user.password,
                                                       'first_name': user.first_name,
                                                       'last_name': user.last_name, 'address': user.address,
                                                       'tel': user.tel, 'passed_test': user.passed_test,
                                                       'pending_tests': user.pending_tests}})
                loading_toJSON(user_data, USERS_FILE_DIRECTORY)

    elif main_choice == 2:
        admin = Admin('', '')
        if not os.path.isfile(f'{ADMIN_FILE_DIRECTORY}.json') or admin_data == None or 'password' not in admin_data or 'login' not in admin_data:
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

                admin = Admin(admin_data['login'],admin_data['password'])

                print('1.Сhange login details\n2.User management\n3.View statistics\n4.Test management\n5.Return to menu above')
                admin_choise = int(input('Choose: '))
                while admin_choise != 5:
                    if admin_choise == 1:
                        print('1.Change login\n2.Change password')
                        admin_choise_change_login_details = int(input('Choose: '))
                        if admin_choise_change_login_details == 1:
                            admin.login = input('write a new login: ')
                            admin_data['login'] = admin.login
                        elif admin_choise_change_login_details == 2:
                            admin.password = input('write a new password: ')
                            admin_data['password'] = admin.password
                        else: print('Incorrect choise')
                        loading_toJSON(admin_data, ADMIN_FILE_DIRECTORY)

                    if admin_choise == 2:
                        print('1.Creat new user\n2.Delete user\n3.Change user')
                        admin_choise_change_user = int(input('Choose: '))
                        user = User('', '', '', '', '', '')
                        if admin_choise_change_user == 1:
                            user.login = input('please write login: ')
                            user.password = input('please write password: ')
                            user.first_name = input('please write first name: ')
                            user.last_name = input('please write last name: ')
                            user.address = input('please write address: ')
                            user.tel = input('please write tel: ')
                            user_data.update({len(user_data) + 1: {'login': user.login, 'password': user.password,
                                                                   'first_name': user.first_name,
                                                                   'last_name': user.last_name, 'address': user.address,
                                                                   'tel': user.tel, 'passed_test': user.passed_test,
                                                                   'pending_tests': user.pending_tests}})
                        elif admin_choise_change_user == 2:
                            user_del = str(hashlib.md5(input('Please write login user then to delete him: ').encode('ascii')).digest())
                            check = [user_data[i]['login'] for i in user_data.keys()]
                            if user_del in check:
                                print('нашли сейчас удалим')
                                user_data.pop(str(check.index(user_del)+1))
                            else:
                                print('user does not exist')
                        elif admin_choise_change_user == 3:
                            user_change = str(hashlib.md5(input('Please write login user then to change him data: ').encode('ascii')).digest())
                            check = [user_data[i]['login'] for i in user_data.keys()]
                            if user_change in check:
                                print('нашли сейчас будем делать изменения')
                                print(user_data[str(check.index(user_change)+1)].values)
                                print('what item do you want to change?')
                                print('1.login\n2.password\n3.First name\n4.Last name\n5.Address\n6.Tel\n7.Passed test\n8.Pending test')

                            else:
                                print('user does not exist')
                        else:print('Incorrect choise')
                        loading_toJSON(user_data, USERS_FILE_DIRECTORY)


                    if admin_choise == 3:
                        pass
                    if admin_choise == 4:
                        test = Test('','','')
                        test.section = input('Write section to test')
                        test.exam_name = input('Write exam name')
                        test.test_dict = {1:{'question':'how many continents',
                                             'answer': ['1','3','6'],
                                             'true_answer': '6'}}



                        # test.test_dict =

                    print('1.Сhange login details\n2.User management\n3.View statistics\n4.Test management\n5.Return to menu above')
                    admin_choise = int(input('Choose: '))
            else:
                print('Incorrect login or password')

    else: print('Incorrect choise')

    main_choice = int(input('Choose: '))

