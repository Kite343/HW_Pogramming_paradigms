""" Таблица умножения
● Условие
  На вход подается число n.
● Задача
  Написать скрипт в любой парадигме, который выводит на экран таблицу умножения всех чисел от 1 до n.
  Обоснуйте выбор парадигм.
● Пример вывода:
1 * 1 = 1
1 * 2 = 2
1 * 3 = 3
1 * 4 = 4
1 * 5 = 5
1 * 6 = 6
..
1 * 9 = 9
"""

"""Так как код должен иметь возможность быть применненным для любого введенго числа,
а для решения задачи есть достаточно времени, то удобнее использовать процедурную (код оформлен в виде процедуры) 
и структурную парадигмы (используется for и нет goto),
так как такой код легче читать, легче реализовывать разбивая на подзадачи и есть возможность повторного применений"""

column = 4

def multiplication_table(n: int):
    mult_table_list = []
    for i in range(1, n + 1):
        n_list = []
        for j in range(1, 10):
            n_list.append(f'{i} * {j} = {i * j}')
        mult_table_list.append(n_list)
    return mult_table_list

def print_multiplication_table(n: int) -> None:
    mult_table_list = multiplication_table(n)
    start, stop = 0, column - 1
    for _ in range(n//column):
        row = mult_table_list[start : stop + 1]
        for i in range(0, 9):
            for j in range(0, column):
                print(row[j][i] + '\t', end='')
            print()
        print()
        start += column
        stop += column
    if start <= n - 1:
        row = mult_table_list[start :]
        for i in range(0, 9):
            for j in range(0, n - start):
                print(row[j][i] + '\t', end='')
            print()
        print()

if __name__ == '__main__':
    n = int(input('Введите число n, до которого будет выведена таблица умножения: '))
    print_multiplication_table(n)