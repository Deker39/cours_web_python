num = int(input('Enter size: '))
for x in range(1,4):
        for j in range(1, 5):
                print('* '*num + '_ '*num,end='')
        print('\n')
for x in range(1, 4):
        for j in range(1, 5):
                print('_ ' * num + '* ' * num, end='')
        print('\n')
