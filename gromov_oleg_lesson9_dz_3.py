
class Worker:
    def __init__(self):
        self.name = ''
        self.surname = ''
        self.position = ''
        self._income = {'wage': 100000, 'bonus': 25000}


class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        #print(self._income['wage'])
        return self._income['wage'] + self._income['bonus']

position1 = Position()

# Получение полного имени.
position1.name = 'Inav'
position1.surname = 'Ivanov'
print(position1.get_full_name())

# значение _income по умолчанию.
print(f' Доход сотрудника {position1.get_full_name()} равен {position1.get_total_income()}.')

# изменяем значение _income
position1._income = {'wage': 110000, 'bonus': 35000}
print(f' Доход сотрудника {position1.get_full_name()} равен {position1.get_total_income()}.')

