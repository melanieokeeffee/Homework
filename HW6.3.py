# 3. Реализовать базовый класс Worker (работник), в котором
# определить атрибуты: name, surname, position (должность),
# income (доход). Последний атрибут должен быть защищенным и
# ссылаться на словарь, содержащий элементы: оклад и премия,
# например, {"wage": wage, "bonus": bonus}. Создать класс
# Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного
# имени сотрудника (get_full_name) и дохода с учетом
# премии (get_total_income).
# Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    def __init__(self, name, surname, position, salary, extra):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"salary": salary, "extra": extra}


class Position(Worker):
    def __init__(self, name, surname, position, salary, extra):
        super(Position, self).__init__(name, surname, position, salary, extra)

    def get_full_name(self):
        return self.name + " " + self.surname

    def get_total_income(self):
        return self._income.get('salary') + self._income.get('extra')


a = Position('Harry', 'Styles', 'singer', 100000, 25000)
print(a.get_full_name())
print(a.position)
print(a.get_total_income())
