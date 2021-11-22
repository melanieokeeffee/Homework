# 1. Создать программно файл в текстовом формате,
# записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.
#

my_list = []
while True:
    lines = input("write something: ")
    if lines == "":
        print(my_list)
        exit()
    else:
        newline = lines + '  /n'
        my_list.append(newline)
    with open(f"HW51.txt", "w+") as HW51:
        HW51.writelines(my_list)

