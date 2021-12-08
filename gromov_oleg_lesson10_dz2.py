from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, param):
        self.param = param

    @abstractmethod
    def calculate(self):
        pass


class Coat(Clothes):

    @property
    def calculate(self):
        return round(((self.param / 6.5) + 0.5), 2)


class Suit(Clothes):

    @property
    def calculate(self):
        return round(((2 * self.param) + 0.3), 2)


# Проверка работы без декоратора @property
class Trousers(Clothes):

    def calculate(self):
        return round(((3 * self.param) + 1.3), 2)


v = 50
h = 156

coat1 = Coat(v)
print(f'Для пальто {v} размера необходимо ткани: {coat1.calculate}')

suit1 = Suit(h)
print(f'Для костюма {h} размера необходимо ткани: {suit1.calculate}')

print(f'Общий расход ткани равняется: {suit1.calculate + coat1.calculate}')

trousers1 = Trousers(124)
print(trousers1.calculate())
