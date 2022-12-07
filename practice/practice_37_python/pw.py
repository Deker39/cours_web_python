#Exercise 1
def first():
    st = str(input('Enter you string: '))
    print(st[::-1])

#Exercise 2
def second():
    s = 0
    g = 0
    st = str(input('Enter you string: '))
    for i in st:
        if i.isdigit():
            g +=1
        else:
            s +=1
    print(f'Number in a word: {g}\nLetters in a word: {s}')

#Exercise 3
def third():
    st =str(input('Enter you string: '))
    w = str(input('Enter you symbol: '))
    print(f"Your simbol meet {sum([1 for i in st if i == w])} times")

#Exercise 4
def fouth():
    st = str(input('Enter you string: '))
    word = str(input('Enter you word: '))
    print(f"Your word meet {sum([1 for i in st.split() if i == word])} times")
#Exercise 5
def fifth():
    st = str(input('Enter you string: '))
    word = str(input('Enter you word: '))
    new_word = str(input('Enter you word for replace: '))
    print(' '.join([new_word if i == word else i for i in st.split()]))

# first()
# second()
# third()
# fouth()
# fifth()