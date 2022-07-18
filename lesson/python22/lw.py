def funn():
    count = []
    str = 'aabBcde'
    str = str.lower()

    for i in str:
        count.append(str.index(i))

    kek = [count[i] for i in range(len(count)) if not i == count.index(count[i])]

    if kek:
        print(f'{str} -> {len(kek)}')
        for i in range(len(kek)):
            print(f'\'{str[kek[i]]}\' - occurs twice')
    else:
        print(f'{str} -> 0')

funn()