# -*- coding: utf8 -*-
# 5. Создать (программно) текстовый файл,
# записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и
# выводить ее на экран.


with open('HW55.txt', 'w+') as HW55:
    line = input('Введите цифры через пробел \n')
    HW55.writelines(line)
    my_numb = line.split()

    print(sum(map(int, my_numb)))