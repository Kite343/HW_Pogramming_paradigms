# Написать скрипт для расчета корреляции Пирсона между двумя случайными величинами (двумя массивами).


from math import sqrt


def pearson_correlation(x_list: list, y_list: list):
    """Функция вычисления коэффициента корреляции Пирсона"""

    def average(lst, n):
        # вычисление среднего значения
        return sum(lst)/n

    def difference_values(lst: list, n: int):
        # список разниц чисел входящего списка со средним значением этого списка
        return list(map(lambda x: x - n, lst))
    
    def root_sum_squares(lst: list):
        # корень из суммы квадратов чисел списка
        return sqrt(sum(map(lambda x: x**2, lst)))

    n_len = len(x_list)
    x_average = average(x_list, n_len)
    y_average = average(y_list, n_len)
    x_diff_list = difference_values(x_list, x_average)
    y_diff_list = difference_values(y_list, y_average)
    numerator = sum(map(lambda xy: xy[0] * xy[1], zip(x_diff_list, y_diff_list)))
    denominator = root_sum_squares(x_diff_list) * root_sum_squares(y_diff_list)

    return numerator / denominator
