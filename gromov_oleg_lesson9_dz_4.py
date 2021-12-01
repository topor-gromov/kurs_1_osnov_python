class Car:
    def __init__(self, is_police = False):
        self.speed = 90
        self.color = 'black'
        self.name = 'Ford'
        self.is_police = is_police

    def go(self):
        print('Автомобиль поехал!')

    def stop(self):
        print('Автомобиль остановился!')

    def turn(self, direction):
        if direction == 'left':
            print('Автомобиль повернул налево!')
        elif direction == 'right':
            print('Автомобиль повернул направо!')
        else:
            print('Указано некорректное направление поворота!')

    def show_speed(self, speed):
        print(f'Скорость движения автомобиля равна {speed} км/ч')


class TownCar(Car):
    def __init__(self, name, color, speed, is_police):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def show_speed(self, speed):
        if speed > 60:
            print('Зафиксированно превышение разрешенной скорости!')



class WorkCar(Car):
    def __init__(self, name, color, speed, is_police):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def show_speed(self, speed):
        if speed > 40:
            print('Зафиксированно превышение разрешенной скорости!')


class SportCar(Car):
    def __init__(self, name, color, speed, is_police):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police
        print('Это спортивный автомобиль! Будьте внимательны на дороге!')


class PoliceCar(Car):

    def __init__(self, name, color, speed, is_police):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police
        print('Это автомобиль полиции!')



car1 = Car(False)
print(f'Марка автомобиля: {car1.name}, цвет: {car1.color}.')
print(f'Автомобиль полиции: {car1.is_police}')
print(f'Разрешенная скорость движения: {car1.speed} км/ч.')
car1.go()
car1.stop()
car1.go()
car1.show_speed(56)
car1.turn('left')
car1.turn('right')

print('---------------------------------')
car2 = Car(False)
car2.speed = 80
car2.name = 'Toyota'
car2.color = 'white'
print(f'Марка автомобиля: {car2.name}, цвет: {car2.color}.')
print(f'Автомобиль полиции: {car2.is_police}')
print(f'Разрешенная скорость движения: {car2.speed} км/ч.')
car2.go()
car2.stop()
car2.go()
car2.show_speed(65)
car2.turn('left')
car2.turn('right')

print('---------------------------------')
car3 = SportCar('Ferrari', 'red', 190, False)
print(f'Марка автомобиля: {car3.name}, цвет: {car3.color}.')
print(f'Автомобиль полиции: {car3.is_police}')
print(f'Разрешенная скорость движения: {car3.speed} км/ч.')
car3.go()
car3.stop()
car3.go()
car3.show_speed(165)
car3.turn('left')
car3.turn('right')

print('---------------------------------')
car4 = WorkCar('MAZ', 'yellow', 40, False)
print(f'Марка автомобиля: {car4.name}, цвет: {car4.color}.')
print(f'Автомобиль полиции: {car4.is_police}')
print(f'Разрешенная скорость движения: {car4.speed} км/ч.')
car4.go()
car4.stop()
car4.go()
car4.show_speed(65)
car4.turn('left')
car4.turn('right')

print('---------------------------------')
car5 = TownCar('KAMAZ', 'green', 60, False)
print(f'Марка автомобиля: {car5.name}, цвет: {car5.color}.')
print(f'Автомобиль полиции: {car5.is_police}')
print(f'Разрешенная скорость движения: {car5.speed} км/ч.')
car5.go()
car5.stop()
car5.go()
car5.show_speed(65)
car5.turn('left')
car5.turn('right')

print('---------------------------------')
car6 = PoliceCar('Ford', 'black', 90, True)
print(f'Марка автомобиля: {car6.name}, цвет: {car6.color}.')
print(f'Автомобиль полиции: {car6.is_police}')
print(f'Разрешенная скорость движения: {car6.speed} км/ч.')
car6.go()
car6.stop()
car6.go()
car6.show_speed(65)
car6.turn('left')
car6.turn('right')