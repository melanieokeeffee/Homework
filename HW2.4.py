# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

first_str = input("Write a sentence ")
numbers = []
num = 1
for i in range(first_str.count(' ') + 1):
    numbers = first_str.split()
    if len(str(numbers)) <= 10:
        print(f" {num} {numbers [i]}")
        num += 1
    else:
        print(f" {num} {numbers [i] [0:10]}")
        num += 1
