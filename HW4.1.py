# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

# первый варииант
from sys import argv

name, worked_hour, rate, benefit = argv
try:
    worked_hour = int(worked_hour)
    rate = int(rate)
    benefit = int(benefit)
    salary = worked_hour * rate + benefit
    print(f'Salary is {salary}')

except ValueError:
    print('Not a number')

# второй вариант

def salary():
    worked_hour = float(input('Введите количество отработанных часов : '))
    rate = float(input('Введите суммы оплаты труда за 1 час : '))
    benefit = float(input('Укажите размер премии - '))
    salary = worked_hour * rate
    return salary + benefit


print(f'Размер заработной платы составил: {salary()}')