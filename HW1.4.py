# 4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

user_number = int(input('write a number in a range [10;infinity] '))
if user_number > 10:
    max = user_number % 10
    while user_number >= 1:
        user_number = user_number // 10
        if user_number % 10 > max:
            max = user_number % 10
        if user_number > 9:
            continue
        else:
            print("Max number is: ", max)
            break
elif user_number < 10:
    print("number isn't in range [10;infinity]")