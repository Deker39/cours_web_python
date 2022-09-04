import random

import requests

response = requests.get("https://randomuser.me/api/?results=25")

users = []

json = response.json()['results']

i = 0
while i < len(json):
	name = json[i]['name']
	original_id = json[i]['id']['value']
	r_id = random.randint(1000, 10000)
	id = str(json[i]['id']['value']).ljust(20) if original_id is not None and original_id.isdigit()  \
		else str(r_id).ljust(20)

	if json[i]["id"]["value"] is None:
		json[i]["id"]["value"] = r_id

	full_name = id + name['title'].ljust(20) + name['first'].ljust(20) + name['last'].ljust(20)
	users.append(full_name)
	i += 1

print("ID".ljust(20) + "Title".ljust(20) + "First".ljust(20) + "Last".ljust(20))
for i in users:
	print(i)

user_to_find = input("Enter id: " )

# Доробити програму - добавити можливість просмотру даних аккаунта по id*
# Користувач вводить id аккаунта та повинен побачити street, city, state, country, email, login, password
