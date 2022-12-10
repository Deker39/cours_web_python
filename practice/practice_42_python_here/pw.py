#Exercise1
def power(arr,c):
    if c == 1:
        return arr
    if c != 1:
        return arr * power(arr,c - 1)

#Exercise2
ls_second = []
def second(a,b):
    if b <= a:
        ls_second.append(f'{a}+')
        return  a
    else:
        ls_second.append(f'{b}+')
        return  b + second(a,b-1)


#Exercise3
ls_third = []
def third(n,c = 1):
    if c <= n:
        print(f'{c} -> {c*"*"}')
        ls_third.append('*')
        third(n,c + 1)


#Exercise4
def mytictactoe(val):
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(val[0], val[1], val[2]))
    print('\t_____|_____|_____')

    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(val[3], val[4], val[5]))
    print('\t_____|_____|_____')

    print("\t     |     |")

    print("\t  {}  |  {}  |  {}".format(val[6], val[7], val[8]))
    print("\t     |     |")
    print("\n")



#Exercise5
#Exercise6

# print(f'power 5^3 = {power(5,3)}')
# print(f'sum recursion:{second(1,5)}')
# print(f'{"".join(ls_second)[:-1]} = {second(1,5)}')
# third(5)
# print(*ls_third)
mytictactoe(['x','x','x','x','x','x','x','x','x'])