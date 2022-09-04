import random

words = ['apple','juice','morning','guese']
word = random.choice(words)
attempts = 15
used_letter = []

guessed_word = ['_' for i in range(len(word))]

print(*guessed_word)
print(word)

while attempts > 0:
    guessed_letter = str(input('Enter letter: '))
    if word.index(guessed_letter):
        used_letter.append(guessed_letter)
        guessed_word[word.index(guessed_letter)] = guessed_letter
        print(guessed_word)
    else:
        used_letter.append(guessed_letter)
        attempts -= 1
    print(f'chance: {attempts}')
    print(f'used letter: {used_letter}')








#  15 попиток
#  used испоьзваные буквы
#  маси слов
# колт=ичесво угаданых слов






# def main():
#     print('gallows')








# if __name__ == '__main__':
#     main()