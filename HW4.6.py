# 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка,
# определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.
#  Обратите внимание, что создаваемый цикл не должен быть бесконечным.
#   Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа,
#  начиная с 3, а при достижении числа 10 завершаем цикл.
#   Во втором также необходимо предусмотреть условие,
#    при котором повторение элементов списка будет прекращено.

from itertools import count, cycle
# вариант а, оба варианта можно сделать с input
for el in count(1):
    if el > 999:
        break
    else:
        print(el)

# вариант б
my_list = [True, 'ABC', 123, None]
for i in cycle(my_list):
    print(i) # цикл бесконечен!