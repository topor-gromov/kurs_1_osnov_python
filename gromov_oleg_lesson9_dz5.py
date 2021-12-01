class Stationery:
    def __init__(self):
        self.title = 'None'

    def draw(self):
        print(f'Запуск отрисовки {self.title}.')

class Pen(Stationery):
    def draw(self):
        print(f'Запуск отрисовки Ручка.')

class Pencil(Stationery):
    def draw(self):
        print(f'Запуск отрисовки Карандаш.')

class Handle(Stationery):
    def draw(self):
        print(f'Запуск отрисовки Маркер.')


stationery1 = Stationery()
stationery1.title = 'Кисть'
stationery1.draw()

pen1 = Pen()
pen1.draw()

pencil1 = Pencil()
pencil1.draw()

handle1 = Handle()
handle1.draw()