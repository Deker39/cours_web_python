# Exercise1
import itertools
import random


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
def third(n, c=1):
    if c <= n:
        print(f'{c} -> {c * "*"}')
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


def myscoreboard(scoreboard):
    print("\t--------------------------------")
    print("\t         SCORE BOARD       ")
    print("\t--------------------------------")

    listofplayers = list(scoreboard.keys())
    print(f"\t{listofplayers[0]}{25 * ' '}", end=f'{scoreboard[listofplayers[0]]}\n')
    print(f"\t{listofplayers[1]}{25 * ' '}", end=f'{scoreboard[listofplayers[1]]}\n')

    print("\t--------------------------------\n")


def fouth():
    print('Frist Player')
    FirstPlayer = input('Specify the Name: ')
    print('\n')

    print('Second Player')
    SecondPlayer = input('Specify the Name: ')
    print('\n')

    curplayer = FirstPlayer
    playerchoice = {'X': '', 'O': ''}
    opt = ['X', 'O']
    scorebord = {FirstPlayer: 0, SecondPlayer: 0}
    myscoreboard(scorebord)
    # Loop for a series of Tic-Tac-Toe game
    # The loop executes until the players quit
    while True:
        # Main Menu for Players
        print(curplayer, "will make the choice:")
        print("Press 1 for X")
        print("Press 2 for O")
        print("Press 3 to Quit")

        # Try exception for THE_CHOICE input
        try:
            the_choice = int(input())
        except ValueError:
            print("Invalid Input!!! Try Again\n")
            continue

            # Conditions for player choice
        if the_choice == 1:
            playerchoice['X'] = curplayer
            if curplayer == FirstPlayer:
                playerchoice['O'] = SecondPlayer
            else:
                playerchoice['O'] = FirstPlayer

        elif the_choice == 2:
            playerchoice['O'] = curplayer
            if curplayer == FirstPlayer:
                playerchoice['X'] = SecondPlayer
            else:
                playerchoice['X'] = FirstPlayer

        elif the_choice == 3:
            print("The Final Scores")
            myscoreboard(scorebord)
            break

        else:
            print("Invalid Selection!! Try Again\n")
        # Storing the winner in a single game of Tic-Tac-Toe
        win = singlegame(opt[the_choice - 1])

        # Updation of the scoreboard as per the winner
        if win != 'D':
            playerWon = playerchoice[win]
            scorebord[playerWon] = scorebord[playerWon] + 1

        myscoreboard(scorebord)
        # Switching player who chooses X or O
        if curplayer == FirstPlayer:
            curplayer = SecondPlayer
        else:
            curplayer = FirstPlayer


# Exercise5
def reference_lsit(val):
    return all(a - b == 1 for a, b in zip(val[1:], val))


def show(index,ls_value,min_ls):
    if index and ls_value:
        for i, y in zip(index, ls_value):
            print(f'{i}: {y} -> {sum(y)}')
            min_ls.append(sum(y))

        print(f'min: {min(min_ls)} -> {ls_value[min_ls.index(min(min_ls))]} value {ls_fifth[min_ls.index(min(min_ls))]}')
    else:
        print('no matches')


ls_fifth = [a[0] for a in itertools.groupby([random.randint(0, 10) for i in range(0, 100)])]
# ls_fifth = [i for i in range(3, 20)]
# print(ls_fifth)
index = []
ls_value = []
min_ls = []


def fifth(org_list):

    if reference_lsit(org_list[0:10]):
        index.append(org_list[0])
        ls_value.append(org_list[0:10])
    if len(org_list) <= 10:
        show(index,ls_value,min_ls)
        return
    fifth(org_list[1:])


# Exercise6

#exer1
# print(f'power 5^3 = {power(5,3)}')
#exer2
# print(f'sum recursion:{second(1,5)}')
# print(f'{"".join(ls_second)[:-1]} = {second(1,5)}')
#exer3
# third(5)
#exer4
# fouth()
#exer5
fifth(ls_fifth)