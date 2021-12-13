# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа
# должна корректно обработать эту ситуацию и не завершиться с ошибкой.
class DivisionByNull:
    def __init__(self, divisible, divider):
        self.divider = divider
        self.divisible = divisible

    @staticmethod
    def divide_by_null(divisible, divider):
        try:
            return (divisible / divider)
        except:
            return (f"You can't divide by zero")


div = DivisionByNull(10, 100)
print(DivisionByNull.divide_by_null(10, 1))
print(DivisionByNull.divide_by_null(10, 0.1))
print(div.divide_by_null(100, 0))