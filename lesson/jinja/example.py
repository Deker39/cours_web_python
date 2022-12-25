from jinja2 import *
from markupsafe import escape


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def getName(self):
#         return  self.name
#
#     def getAge(self):
#         return  self.age

# per = Person('Frodo',22)
# per = {'name':'Frodo','age':22}
# tm = Template('i\'m {{p["age"]}} old, hello {{p.name}}')
# msg = tm.render(p=per)
#
# print(msg)

# data = '''{% raw %}Modul Jinja instead of
# definitions {{ name }}
# substituting the corresponding value{% endraw %}'''

# data ='''In HTML- document link definitions as:
# <a href="#">Link</a>'''

# tm = Template('{{data | e}}')
# msg = tm.render(data=data)
# msg = escape(data)
# print(msg)

# cities = [{'id':1, 'city': 'Kiev'},
#           {'id':5, 'city': 'Odessa'},
#           {'id':7, 'city': 'Kherson'},
#           {'id':8, 'city': 'Dnipro'},
#           {'id':11, 'city': 'Lviv'}]
#
# link = '''<select name="cities">
# {% for c in cities -%}
# {% if c.id > 6 -%}
#     <option value="{{c["id"]}}">{{c["city"]}}</option>
# {% else -%}
#     {{c['city']}}
# {% endif -%}
# {% endfor -%}
# </select>'''
# tm = Template(link)
# msg = tm.render(cities=cities)
# print(msg)

# cars  = [
#     {'model': 'Audi', 'price': 23000},
#     {'model': 'Shkoda', 'price': 17300},
#     {'model': 'Volvo', 'price': 44300},
#     {'model': 'VoltcWagen', 'price': 21300}
# ]
# ##TODO sum
# # tpl1 = 'Summer price cars {{ cs | sum(attribute="price")}}'
# ##TODO max
# # tpl1 = 'Summer price cars {{ cs | max(attribute="price")}}'
# ##TODO min
# # tpl1 = 'Summer price cars {{ (cs | min(attribute="price")).model}}'
# ##TODO rand
# tpl1 = 'Summer price cars {{ cs | random }}'
# ##TODO replace
# tpl1 = 'Summer price cars {{ cs | replace("o", "O") }}'
#
# # digs = [1,2,3,4,5]
# # tpl2 = 'Summer price cars {{ cs | sum}}'
#
# tm = Template(tpl1)
# msg = tm.render(cs = cars)
# print(msg)
#
# #TODO upper
# persons = [
#     {'name': 'Alex', 'old': 18, 'weigth': 78.5},
#     {'name': 'Den', 'old': 28, 'weigth': 82.5},
#     {'name': 'Jhon', 'old': 3, 'weigth': 94.5}
# ]
#
# tpl = '''
# {%- for u in user -%}
# {% filter upper %}{{ u.name }}{% endfilter%}
# {% endfor -%}
# '''
#
# tm = Template(tpl)
# msg = tm.render(user=persons)
#
# print(msg)
#
#TODO templet macro input

# html = '''
# {% macro input(name, value='', type='text', size=20) -%}
#     <input type="{{ type }}" name="{{ name }}" value="{{ value|e }}" size="{{ size }}">
# {%- endmacro %}
#
# <p>{{ input('usernmae') }}</p>
# <p>{{ input('email') }}</p>
# <p>{{ input('password') }}</p>
# '''
#
# tm = Template(html)
# msg = tm.render()
# print(msg)

##TODO templat macro ul
# persons = [
#     {'name': 'Alex', 'old': 18, 'weigth': 78.5},
#     {'name': 'Den', 'old': 28, 'weigth': 82.5},
#     {'name': 'Jhon', 'old': 3, 'weigth': 94.5}
# ]
# html='''
# {% macro list_user(list_of_user) -%}
# <ul>
# {%- for u in list_of_user %}
#     <li>{{ u.name }} {{ caller(u)}}</li>
# {%- endfor %}
# </ul>
# {%- endmacro %}
#
# {% call(user) list_user(users) %}
#     <ul>
#     <li>age: {{user.old}}</li>
#     <li>weight: {{user.weight}}</li>
#     </ul>
# {% endcall -%}
# '''
#
# tm = Template(html)
# msg = tm.render(users=persons)
# print(msg)
# ## TODO Environment FileSystemLoader
# persons = [
#     {'name': 'Alex', 'old': 18, 'weigth': 78.5},
#     {'name': 'Den', 'old': 28, 'weigth': 82.5},
#     {'name': 'Jhon', 'old': 3, 'weigth': 94.5}
# ]
#
# # file_load = FileSystemLoader('templates')
# # env = Environment(loader=file_load)
# #
# # tm = env.get_template('main.html')
# # msg = tm.render(users=persons)
# #
# # print(msg)
#
# ##TODO Environment FunctionLoader
# def loadTpl(path):
#     if path == 'index':
#         return '''Name {{ u.name}}, age {{u.old}}'''
#     else:
#         return '''Date: {{u}}'''
#
# file_load = FunctionLoader(loadTpl)
# env = Environment(loader=file_load)
#
# tm = env.get_template('index')
# msg = tm.render(u=persons[0])
#
# print(msg)
## TODO include and import
#
# file_load = FileSystemLoader('templates')
# env = Environment(loader=file_load)
#
# tm = env.get_template('page.htm')
# msg = tm.render(domain='http://google.com', title='About Jinja')
#
# print(msg)
## TODO extension templates
items = ['math','history','physics','chemistry']

file_load = FileSystemLoader('templates')
env = Environment(loader=file_load)
tm = env.get_template('about.htm')
output = tm.render(list_table=items)
print(output)

