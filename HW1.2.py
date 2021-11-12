
# 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды
# и выведите в формате чч:мм:сс. Используйте форматирование строк.


user_seconds = int(input('Write a number of seconds'))
# находим, сколько останется секунд, которые не перейдут в минуты
seconds = user_seconds % 60
print(seconds)

# находим целое количество минут
left_in_minutes = user_seconds // 60
# находим, сколько останется минут, которые не перейдут в часы
minutes = left_in_minutes % 60
print(minutes)

# находим количество часов
hours = left_in_minutes // 60
print(hours)

print(f'The answer is {hours:02}:{minutes:02}:{seconds:02}')