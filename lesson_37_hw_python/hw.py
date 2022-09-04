import random
#
# words = ['apple','juice','morning','guese']
# word = random.choice(words)
# used_letter = []
# attempts = 15
# win = 0
#
# guessed_word = ['_' for i in range(len(word))]
#
# print(*guessed_word)
# print(word)
#
# while attempts != 0:
#     if ''.join(guessed_word) == word:
#         print('you win')
#         win =+ 1
#         break
#     else:
#         guessed_letter = str(input('Enter letter: '))
#         if guessed_letter in used_letter:
#             print('you used this letter')
#             guessed_letter = str(input('Enter letter: '))
#
#         else:
#             if len(guessed_letter) > 1:
#                 if guessed_letter == word:
#                     print('you win')
#                     break
#
#             if word.find(guessed_letter) >= 0:
#                 used_letter.append(guessed_letter)
#                 for i in [i for i in range(len(word)) if word[i] == guessed_letter]:
#                     guessed_word[i] = guessed_letter
#
#             else:
#                 used_letter.append(guessed_letter)
#                 attempts -= 1
#
#         print(*guessed_word)
#         print(f'chance: {attempts}')
#         print(f'used letter: {" ".join(used_letter)}')
#
# else: print('you lose')

#  15 попиток
#  used испоьзваные буквы
#  маси слов
# колт=ичесво угаданых слов

def random_word(arr):
    return random.choice(arr)

def result(guessed_word,attempts,used_letter):
    print(*guessed_word)
    print(f'chance: {attempts}')
    print(f'used letter: {" ".join(used_letter)}')

def check_word(let):
    if word.find(guessed_letter) >= 0:
        used_letter.append(guessed_letter)
        for i in [i for i in range(len(word)) if word[i] == guessed_letter]:
            guessed_word[i] = guessed_letter
        return 0

    else:
        used_letter.append(guessed_letter)
        return -1

def restar(word):
    return ['_' for i in range(len(word))]

words = ['apple','juice','morning','guese']
word = random_word(words)
used_letter = []
attempts = 15
win = 0
guessed_word = restar(word)

print(*guessed_word)
print(word)

while attempts != 0 and len(words) > 0:
    if ''.join(guessed_word) == word:
        words.remove(word)
        win = + 1
        print(f'you win: {win}')
        word = random_word(words)
        guessed_word = restar(word)
        print(*guessed_word)
        print(word)

    else:
        guessed_letter = str(input('Enter letter: '))
        if guessed_letter in used_letter:
            print('you used this letter')
            guessed_letter = str(input('Enter letter: '))

        if len(guessed_letter) > 1:
            if guessed_letter == word:
                words.remove(word)
                win = + 1
                print(f'you win: {win}')
                word = random_word(words)
                guessed_word = restar(word)
                print(*guessed_word)
                print(word)

        attempts = attempts + check_word(guessed_letter)

        result(guessed_word,attempts,used_letter)


else: print('you lose')



