#Exercise 1
def first():
    pm = g = e = 0
    # g = 0
    # e = 0
    st = str(input('Enter you string: '))
    for i in st:
        if i.isdigit():
            g += 1
        elif i == '!':
            e += 1
        elif i == ',':
            pm += 1

    print(f'{st.split(".")[0]}.',' '.join([y.title() for y in [f'{i}.' if i != st.split('.')[-1] else i for i in st.split('.')][1:]]))
    print(f'Number in a string: {g}\n'
          f'Punctuation mark in a string: {pm}\n'
          f'Exclamatory mark in a string: {e}')
#Exercise 2
def second():
    pass
#Exercise 3
def third():
    pass
first()