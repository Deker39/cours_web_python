import random

indef_code = [random.randint(1000,9999) for i in range(0,10)]
tel = ['+380' + str(random.randint(550000000,999999999)) for i in range(0,10)]

mixed = []
[mixed.append([i,j]) for i,j in zip(indef_code,tel)]

for i in range(0, len(mixed)):
    print(f'{i+1}', end='\t')
    for i2 in range(0, len(mixed[i])):
        print(f'{mixed[i][i2]}', end='\t')
    print()


mixed.sort(key = lambda x: x[0])
print(mixed)
mixed.sort(key = lambda x: x[1])
print(mixed)