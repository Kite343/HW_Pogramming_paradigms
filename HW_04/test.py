# pip install numpy
# pip install pandas
from pearson_correlation import pearson_correlation
import random

import numpy as np
import pandas as pd

if __name__ == '__main__':
    for _ in range(int(input("Ведите количество тестов "))):
        n = random.randint(10, 30)
        x_list = [random.randint(-200, 200) for _ in range(n)]
        y_list = [random.randint(-200, 200) for _ in range(n)]
        print('Тестовые данные')
        print(x_list)
        print(y_list)
        print('Значение функции')
        r = pearson_correlation(x_list, y_list)
        print(r)
        print()
        print('проверочное значение полученное numpy')
        np_array_x = np.array(x_list)
        np_array_y = np.array(y_list)
        pearson_corr = lambda x, y: np.corrcoef(x, y)[0, 1]
        r = pearson_corr(np_array_x, np_array_y)
        print(r)
        print('проверочное значение полученное pandas')
        pd_array_x = pd.Series(x_list)
        pd_array_y = pd.Series(y_list)
        print(pd_array_x.corr(pd_array_y))
        print()

# Тестовые данные
# [121, -138, 39, -70, -153, 90, 188, -192, -137, 173, 147, -2, -143]
# [80, -14, 176, -90, 63, -86, -165, 13, -162, 186, 116, 40, -112]
# Значение функции
# 0.30587032845476786

# проверочное значение полученное numpy
# 0.3058703284547678
# проверочное значение полученное pandas
# 0.3058703284547678


# Тестовые данные
# [-148, -189, 37, -132, -158, -134, 130, -85, -86, -69, -71, 7, -157, 47, 75, 6, 150, 14, -169, 27, -180, 73, 110, -39, -35, 148, 126, 6, -128, 33]
# [152, -39, -153, -168, 191, -22, 195, 45, 155, -123, -67, -182, 127, -41, 76, -26, -28, 151, 146, -106, 174, 59, -93, -151, 158, 0, -68, -61, 16, 26]
# Значение функции
# -0.24393123515994625

# проверочное значение полученное numpy
# -0.24393123515994625
# проверочное значение полученное pandas
# -0.24393123515994625


# Тестовые данные
# [179, 72, -2, 123, -174, -129, -41, 176, -54, 196, -141, 75, 148, -164, -56, -89, 200, -11, -103, 155, 190, 137, -25, -190, 154, 116, -10, 178, 32, 155]
# [85, -140, -159, 23, -43, 5, -68, -1, 90, -97, -41, 13, -78, 176, 198, 44, 21, 7, 34, -73, 10, -22, -168, 
# -188, -55, -131, 174, -142, 8, -139]
# Значение функции
# -0.19578407619032312

# проверочное значение полученное numpy
# -0.19578407619032312
# проверочное значение полученное pandas
# -0.19578407619032312


# Тестовые данные
# [155, 154, -86, -142, -129, 24, -194, -81, -133, 158, 169, 174, 174, 39, 196, 80]
# [-173, 105, -40, -21, -82, -58, -151, -161, -70, -41, 131, -200, -188, -144, 100, -165]
# Значение функции
# 0.2019835387659233

# проверочное значение полученное numpy
# 0.20198353876592332
# проверочное значение полученное pandas
# 0.20198353876592332