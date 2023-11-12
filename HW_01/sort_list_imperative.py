# Дан список целых чисел numbers. Необходимо написать в императивном стиле процедуру для
# сортировки числа в списке в порядке убывания. Можно использовать любой алгоритм сортировки.

import random


def sort_list_imperative(numbers: list) -> list:
    # n = len(numbers)
    n = 0
    for _ in numbers:
        n += 1
    for i in range(n - 1):
        for j in range(n - i - 1):
            if numbers[j] < numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers

# array = [1, 7, -3, 9, 0, -67, 34, 12, 45, 100, 6,  8, -2, 99]
# print(array)
# sort_list_imperative(array)
# print(array)

# # test
# a, b = int(input("введите минимальную длину массива ")), int(input("введите максимальную длину массива "))
# n = int(input("введите количество тастов "))
# for _ in range(n):
#     array = [random.randint(-200, 200) for _ in range(random.randint(a, b))]
#     print(*array)
#     sort_list_imperative(array)
#     print(*array)
#     print()