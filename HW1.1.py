# 1 Поработайте с переменными, создайте несколько(age),
# выведите на экран(вывела), запросите у пользователя несколько чисел (user_age and user_number)
# и строк(user_name) и сохраните в переменные, выведите на экран.

age = 'if your age is more than 18 and less 100, please take part'
print(age)

user_name = input('write your name ')
user_age = input('write your age ')
user_number = int(input('write your number '))

print('please check if there is any mistakes')
print(f'Is your name {user_name}?')
print(f'Is your age {user_age}?')
print(f'Is your number {user_number}?')

