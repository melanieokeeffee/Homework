#type_1(Для списка реализовать обмен значений соседних элементов, т.е.
#Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
#При нечетном количестве элементов последний сохранить
#на своем месте.
#Для заполнения списка элементов необходимо использовать
#функцию input()my_str_1)

counting = int(input("Write a number of elements "))  # первый ввод цифры
my_list = []
i = 0
el = 0
while i < counting:
    my_list.append(input("Write a number to put in a list "))
    i += 1
print(my_list)
for elem in range(int(len(my_list)/2)):
        my_list[el], my_list[el + 1] = my_list [el + 1], my_list[el]
        el += 2
print(my_list)
