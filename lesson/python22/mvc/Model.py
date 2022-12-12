import json

class Person:

    def __init__(self, first_name=None, last_name=None):
        self.firstName = first_name
        self.lastName = last_name

    def __str__(self):
        return f"{self.firstName}: {self.lastName}"

    @staticmethod
    def getAll():
        result = []
        with open('db.json',encoding='utf-8') as f:
            data = list(json.loads(f.read()).values())
            for i in data:
                 result.append(Person(i['first_name'],
                                      i['last_name']))
        return result

