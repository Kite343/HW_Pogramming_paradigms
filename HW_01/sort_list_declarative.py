# Написать точно такую же процедуру, но в декларативном стиле

import random


def sort_list_declarative(numbers: list) -> list:
    numbers.sort(reverse=True)
    return numbers

# array = [1, 7, -3, 9, 0, -67, 34, 12, 45, 100, 6,  8, -2, 99]
# print(array)
# sort_list_declarative(array)
# print(array)

# # test
# a, b = int(input("введите минимальную длину массива ")), int(input("введите максимальную длину массива "))
# n = int(input("введите количество тастов "))
# for _ in range(n):
#     array = [random.randint(-200, 200) for _ in range(random.randint(a, b))]
#     print(*array)
#     sort_list_declarative(array)
#     print(*array)
#     print()