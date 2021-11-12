# 5. Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

# запрашиваем выручку и издержки
revenue = float(input("Write company's revenue "))
expenses = float(input("Write company's expenses "))
# формулы в одно место по возможности
profit = revenue - expenses  # прибыль
profitability = float(profit / revenue)  # рентабельность

if revenue > expenses:
    print('The company is earning money')
    print(f'profitability is {profitability}')
    workers = int(input("How many employees do you have? "))
    worker_earn = profit / workers
    print(worker_earn)

elif profit == expenses:
    print("The company doesn't earn money")

else: print('The company is loosing money')