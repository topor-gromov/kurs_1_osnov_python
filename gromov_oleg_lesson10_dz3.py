class Cell():
    def __init__(self, count):
        self.count = count

    def __add__(self, other):
        return self.count + other.count

    def __sub__(self, other):
        sub_cell = self.count - other.count
        if sub_cell > 0:
            return sub_cell
        else:
            return 'Значение меньше нуля!'

    def __mul__(self, other):
        return self.count * other.count

    def __truediv__(self, other):
        return int(self.count / other.count)

    def __floordiv__(self, other):
        return self.count // other.count

    def make_order(self, column):
        result_string = ''
        for i in range(1, self.count + 1):
            result_string = result_string + '*'
            if i / column == i // column:
                result_string = result_string + '\n'

        return result_string


cell1 = Cell(16)
cell2 = Cell(8)
cell3 = Cell(3)

print(f'Результат сложения: {cell1 + cell2}')
print(f'Результат вычитания: {cell1 - cell2}')
print(f'Результат вычитания: {cell2 - cell1}')
print(f'Результат умножения: {cell1 * cell2}')
print(f'Результат деления: {cell1 / cell2}')
print(f'Результат целочисленного деления: {cell1 / cell3}')

print('\nВывод ячеек:\n')

print(cell1.make_order(4))
print(cell2.make_order(2))
