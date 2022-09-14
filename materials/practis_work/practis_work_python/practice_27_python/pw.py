# Exercise1
print(f'\x1B[3mNothing\nwill work\nunless you do.\x1B[3m',end='\n\n')
# Exercise2
print(f'\x1B[3m"Anyone who\x1B[3m',
      f'\t\x1B[3mstops\x1B[3m',
      f'\t\t\x1B[3mlearning is old\x1B[3m',
      f'\t\t\t\x1B[3mwhether at twenty or eighty”.\x1B[3m',
      f'\t\t\t\t\t\t\t\t\t\x1B[3mHenry Ford\x1B[3m',sep='\n',end='\n\n')
# Exercise3
def third():
      num1 = int(input('Enter first value: '))
      num2 = int(input('Enter second value: '))
      print(f'sum of numbers: {num1 + num2}',
            f'difference of numbers: {num1 - num2}',
            f'product of numbers: {num1 * num2}', sep='\n', end='\n\n')
# Exercise4
def fourth():
      num = int(input('Enter number value: '))
      persent = int(input('Enter persent value: '))
      print(f'{persent}% off {num} is {num*persent/100}')
# Exercise5
def fifth():
      width = int(input('Enter width rectangle: '))
      height = int(input('Enter height rectangle: '))
      print(f'area of a rectangle: {width * height}')
