# -*- coding: utf8 -*-
# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу,
# открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый
# блок строк должен записываться в новый текстовый файл.



# with open("Lesson5/HW54.txt", 'r') as f:
#     f.readline()
#     print(f)

# d = {}
# with open("Lesson5/HW54.txt") as f:
#
#     for line in file:
#        key, value = line.split()
#        d[key] = value
# print(d)

translater = {'One': 'odin', 'Two': 'dva', 'Three': 'tri', 'Four': 'chetyre'}
my_list = []
result = []
try:
    file_obj = open("Lesson5/HW54.txt", 'r')
    for line in file_obj:
        tokens = line.split(" - ")
        print(tokens)
        if tokens[0] in translater:
            word = translater[tokens[0]]
            result.append(word +' - '+ tokens[1])
    print(result)
except IOError:
    print("Произошла ошибка ввода-вывода!")
finally:
    file_obj.close()

try:
    file_input = open("Lesson5/HW54.txt", "w")
    file_input.writelines(result)
except IOError:
    print("Произошла ошибка ввода-вывода!")
finally:
    file_input.close()

