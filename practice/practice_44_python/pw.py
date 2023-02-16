import random


# Exercise1
def method_sort_shell(ls):
    gap = len(ls) // 2

    while gap > 0:
        for i in range(gap, len(ls)):
            temp = ls[i]
            j = i
            while j >= gap and ls[j - gap] > temp:
                ls[j] = ls[j - gap]
                j -= gap
            ls[j] = temp
        gap //= 2


# Exercise2
def heapify(sort_nums, heap_size, root):
    l = root
    left = (2 * root) + 1
    right = (2 * root) + 2
    if left < heap_size and sort_nums[left] > sort_nums[l]:
        l = left
    if right < heap_size and sort_nums[right] > sort_nums[l]:
        l = right
    if l != root:
        sort_nums[root], sort_nums[l] = sort_nums[l], sort_nums[root]
        heapify(sort_nums, heap_size, l)


def method_pyramidal_sorting(ls):
    size = len(ls)
    for i in range(size, -1, -1):
        heapify(ls, size, i)
    for i in range(size - 1, 0, -1):
        ls[i], ls[0] = ls[0], ls[i]
        heapify(ls, i, 0)

# Exercise3
def partition(ls, low, high):
    pivot = ls[high]
    i = low - 1
    for j in range(low, high):
        if ls[j] <= pivot:
            i += 1
            (ls[i], ls[j]) = (ls[j], ls[i])
    (ls[i + 1], ls[high]) = (ls[high], ls[i + 1])
    return i + 1

def method_quick_sort(ls, low, high):
    if low < high:
        pi = partition(ls, low, high)
        method_quick_sort(ls, low, pi - 1)
        method_quick_sort(ls, pi + 1, high)

# Exercise4
def sort_cupcake(ls):
    j = 1
    c = 0
    while j > 0:
        print(f'{c}:{ls}')
        for i in range(0, len(ls) - 1):
            if ls[i] > ls[i + 1]:
                ls[i], ls[i + 1] = ls[i + 1], ls[i]
                j += 1
                c += 1
                break

        j -= 1
    print(f'count: {c}')




first_list = [random.randint(0, 100) for q in range(0, 10)]
second_list = [random.randint(0, 100) for w in range(0, 10)]
third_list = [random.randint(0, 100) for e in range(0, 10)]
fourth_list = [random.randint(0, 100) for r in range(0, 10)]
method_sort_shell(first_list)
print(f'Method shell: {" ".join(map(str, first_list))}')
method_pyramidal_sorting(second_list)
print(f'Method pyramidal : {" ".join(map(str, second_list))}')
method_quick_sort(third_list, 0, len(third_list) - 1)
print(f'Method quick sort : {" ".join(map(str, third_list))}')
sort_cupcake(fourth_list)
print(f'cupcake sorted: {" ".join(map(str, fourth_list))}')
