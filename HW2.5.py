# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].


first_list = [7, 5, 3, 3, 2]
print(f'Rating - {first_list}')
number = int(input('Write a number '))
while number != 100:
    for el in range(len(first_list)):
        if first_list[el] == number:
            first_list.insert(el + 1, number)
            break
        elif first_list[0] < number:
            first_list.insert(0, number)
        elif first_list[-1] > number:
            first_list.append(number)
        elif first_list[el] > number and first_list[el + 1] < number:
            first_list.insert(el + 1, number)
        print(f"Rating - {first_list}")
        number = int(input("Write a number "))
