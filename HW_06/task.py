"""Написать программу на любом языке в любой парадигме для
бинарного поиска. На вход подаётся целочисленный массив и
число. На выходе - индекс элемента или -1, в случае если искомого
элемента нет в массиве."""

"""
При решении задачи использованы структурная и процедурная парадигмы
"""

def binary_search(lst: list[int], n: int):
    left = 0
    right = len(lst) - 1

    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == n:
            return mid
        elif n < lst[mid]:
            right = mid - 1
        else:
            left = mid + 1
        
    return -1

if __name__ == '__main__':
    # tests
    test_lst = [1, 4, 7, 9, 12, 13, 15, 17, 19, 20, 21, 34, 37, 39, 45, 81, 110, 135, 168, 190]
    print(f"n = 9 index = {binary_search(test_lst, 9)}")
    # 3
    print(f"n = 17 index = {binary_search(test_lst, 17)}")
    # 7
    print(f"n = 21 index = {binary_search(test_lst, 21)}")
    # 10
    print(f"n = 135 index = {binary_search(test_lst, 135)}")
    # 17
    print(f"n = 1 index = {binary_search(test_lst, 1)}")
    # 0
    print(f"n = 190 index = {binary_search(test_lst, 190)}")
    # 19
    print(f"n = 5 index = {binary_search(test_lst, 5)}")
    # -1




    