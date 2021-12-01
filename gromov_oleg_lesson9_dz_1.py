import time
import termcolor

class TrafficLight:
    def __init__(self):
        self.__color = 'red'
        self.flag_run = True

    def running(self, count):
        count_running = 0
        print('------------------------------')
        while count_running < count:
            self.__color = 'red'
            print(termcolor.colored('Красный сигнал светофора.', self.__color))
            time.sleep(7)
            self.__color = 'yellow'
            print(termcolor.colored('Жёлтый сигнал светофора.', self.__color))
            time.sleep(2)
            self.__color = 'green'
            print(termcolor.colored('Зелёный сигнал светофора.', self.__color))
            time.sleep(7)
            print('------------------------------')
            count_running += 1

try:
    count_run = int(input('Введите количество полных циклов переключения светофора для вывода: '))
    if count_run is not None:
        t1 = TrafficLight()
        t1.running(count_run)
except ValueError:
    print('Некорректное значение!')

