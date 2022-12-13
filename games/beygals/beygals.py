import random

NUM_DIGITS = 3
MAX_GUESSES = 10


def getSecretNum():
    numbers = list('0123456789')
    random.shuffle(numbers)

    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum


def getClues(guess, secretNum):
    pass


def main():
    print(f'''
    Bagels, a deductive logic game.
    By Al Sweigart al@inventwithpython.com
    I am thinking of a {NUM_DIGITS}-digit number with no repeated digits.
    Try to guess what it is. Here are some clues:
    When I say: That means:
        Pico        One digit is correct but in the wrong position.
        Fermi       One digit is correct and in the right position.
        Bagels      No digit is correct.
    For example, if the secret number was 248 and your guess was 843, the
    2 clues would be Fermi Pico.''')

    while True:
        secretNum = getSecretNum()
        print('I have thought up a number.')
        print(f' You have {MAX_GUESSES} guesses to get it.')

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess  = ''
            while len(guess) != MAX_GUESSES or not  guess.isdecimal():
                print(f'Guess #{numGuesses}: ')
                guess = input('> ')

            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break
            if numGuesses > MAX_GUESSES:
                print('You ran out of guesses.')
                print(f'The answer was {secretNum}.')

        print('Do you want to play again? y/n')
        if not input('> ').lower().startswith('y'):
            break
    print('Thanks for playing!')



if __name__ == '__main__':
    main()



