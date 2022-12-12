def index():
    print("MVC - simple example test - index")
    # input('Press [Enter] to see data from data base')
    print('Press [y] to see data from database, [n] - exit : ')

def person(ls):
    print(f"Data from db have {len(ls)} Persons:")
    for item in ls:
        print(item)

def endView():
    print('Goodbye')

