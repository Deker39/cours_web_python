import random


# Exercise 1
def bubble_sort(ls):
    for i in range(len(ls) - 1):
        for j in range(len(ls) - i - 1):
            if ls[j] > ls[j + 1]:
                ls[j], ls[j + 1] = ls[j + 1], ls[j]


# Exercise 2
def insertion_sort(ls):
    for i in range(0, len(ls)):
        key = ls[i]
        j = i - 1
        while j >= 0 and key < ls[j]:
            ls[j + 1] = ls[j]
            j -= 1
        ls[j + 1] = key


# Exercise 3
def descending(ls):
    for i in range(0, len(ls)):
        key = ls[i]
        j = i - 1
        while j >= 0 and key > ls[j]:
            ls[j + 1] = ls[j]
            j -= 1
        ls[j + 1] = key
    return ls


def ascending(ls):
    for i in range(0, len(ls)):
        key = ls[i]
        j = i - 1
        while j >= 0 and key < ls[j]:
            ls[j + 1] = ls[j]
            j -= 1
        ls[j + 1] = key
    return ls


def i_sort(ls):
    mid = len(ls)//2
    l = ls[:mid]
    r = ls[mid:]
    ls = descending(l).append(ascending(r))

# Exercise 4
def merge_sort(ls):
    if len(ls) > 1:
        mid = len(ls) // 2
        l, r = ls[:mid], ls[mid:]
        merge_sort(l)
        merge_sort(r)
        i = j = k = 0
        while i < len(l) and j < len(r):
            if l[i] <= r[j]:
                ls[k] = l[i]
                i += 1
            else:
                ls[k] = r[j]
                j += 1
            k += 1

        while i < len(l):
            ls[k] = l[i]
            i += 1
            k += 1
        while j < len(r):
            ls[k] = r[j]
            j += 1
            k += 1

rand_list = rand_list_one = rand_list_two = rand_list_three = rand_list_fourth \
    = [random.randint(0, 100) for i in range(0, 10)]
print(f'default list: {rand_list}')
# Exercise 1
# bubble_sort(rand_list_one)
# print(f'bubble sort list: {rand_list_one}')
# Exercise 2
# insertion_sort(rand_list_two)
# print(f'insertion sort list: {rand_list_two}')
# Exercise 3
# i_sort(rand_list_three)
# print(f'sort the first half of the list in descending order, the second half in ascending order: {rand_list_three}')
# Exercise 4
# merge_sort(rand_list_fourth)
# print(f'merge sort list: {rand_list_fourth}')
print(f'sorted list:{sorted(rand_list)}')
