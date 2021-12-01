class Road:
    def __init__(self):
        self._length = 5000
        self._width = 20

    def weight(self, weight, thickness):
        result = self._width * self._length * weight * thickness
        print('Масса используемого асфальта, для дорожного полотна:')
        print(f'-- длиной {self._length} метров')
        print(f'-- шириной {self._width} метров')
        print(f'-- толщиной асфальта {thickness} сантиметров')
        print(f'Равна {result / 1000} т.')


road = Road()
road.weight(25, 5)

