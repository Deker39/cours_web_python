# Exercise1
def power(arr, c):
    if c == 1:
        return arr
    if c != 1:
        return arr * power(arr, c - 1)


# Exercise2
ls_second = []


def second(a, b):
    if b <= a:
        ls_second.append(f'{a}+')
        return a
    else:
        ls_second.append(f'{b}+')
        return b + second(a, b - 1)


# Exercise3
ls_third = []


def third(n, c=1):
    if c <= n:
        print(f'{c} -> {c * "*"}')
        ls_third.append('*')
        third(n, c + 1)


# Exercise4
def mytictactoe(val):
    print("\n")
    print("\t     |     |")
    print(f"\t  {val[0]}  |  {val[1]}  |  {val[2]}")
    print('\t_____|_____|_____')

    print("\t     |     |")
    print(f"\t  {val[3]}  |  {val[4]}  |  {val[5]}")
    print('\t_____|_____|_____')

    print("\t     |     |")

    print(f"\t  {val[6]}  |  {val[7]}  |  {val[8]}")
    print("\t     |     |")
    print("\n")


def check_Victory(playerpos, curplayer):
    solution = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

    for i in solution:
        if all(j in playerpos[curplayer] for j in i):
            return True
    return False


def chek_Tie(playerpos):
    if len(playerpos['X']) + len(playerpos['O']) == 9:
        return True
    return False



def singlegame(curplayer):
    val = [' ' for i in range(9)]
    playerpos = {'X': [], 'O': []}

    while True:
        mytictactoe(val)

        try:
            print(f'Plater {curplayer} turn. Choose toyr Block: ', end='')
            chance = int(input())
        except ValueError:
            print('Invalid Input!!! Try again')
            continue

        if chance < 1 or chance > 9:
            print('Invalid Input!!! Try again')
            continue
        if val[chance - 1] != ' ':
            print('Oops! The Place is already occupied. Try again')
            continue

        val[chance - 1] = curplayer
        playerpos[curplayer].append(chance)

        if check_Victory(playerpos, curplayer):
            mytictactoe(val)
            print(f"Congratulations! Player {curplayer} has won the game!\n")
            return curplayer

        if chek_Tie(playerpos):
            mytictactoe(val)
            print('Oh! Game Tied\n')
            return 'D'

        if curplayer == 'X':
            curplayer = 'O'
        else:
            curplayer = 'X'

if __name__ == '__main__':
    print('Frist Player')
    FirstPlayer = input('Specify the Name: ')
    print('\n')

    print('Second Player')
    SecondPlayer = input('Specify the Name: ')
    print('\n')

    curplayer = FirstPlayer
    playerchoice = {'X':'','O':''}
    opt = ['X','O']
    scorebord = {FirstPlayer:0, SecondPlayer: 0}
    mytictactoe(scorebord)

# Exercise5
# Exercise6

# print(f'power 5^3 = {power(5,3)}')
# print(f'sum recursion:{second(1,5)}')
# print(f'{"".join(ls_second)[:-1]} = {second(1,5)}')
# third(5)
# print(*ls_third)
