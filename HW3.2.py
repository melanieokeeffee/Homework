# 2. Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

# способ 1 (Возможно найду второй)

name = input('Write your name: ')
surname = input('Write your surname: ')
birth_year = input('Write your birth_year: ')
city = input('Write a city you live in: ')
email = input('Write your email: ')
phone = input('Write your phone: ')

print(f"name= {name}, surname= {surname}, birth_year= {birth_year}, city= {city}, email= {email}, phone= {phone}")