from mvc.Model import Person
from mvc.View import index, person, endView


def showAll():
    people = Person.getAll()
    return person(people)

def start():
    index()
    answer = input()
    if answer == 'y':
        return showAll()
    else:
        return endView()


if __name__ == '__main__':
    start()