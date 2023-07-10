class Person4:
    __max_up = 3
    _max_level = 80
    def __init__(self, name, race='unknown', speed=100):
        self.name = name
        self.race = race
        self.level = 1
        self.health = 100
        self._speed = speed
        self.up = 3
    def _check_level(self):
        return self.level < self._max_level
    def level_up(self):
        if self._check_level():
            self.level += 1
    def change_health(self, other, quantity):
        self.health += quantity
        other.health -= quantity

    def add_up(self):
        self.up += 1
        self.up = min(self.up, self.__max_up)

class Hero(Person4):
    def __init__(self, power, *args, **kwargs):
        self.power = power
        super().__init__(*args, **kwargs)# получаем от ближайшего класса родителя его аргументы

    def change_health(self, other, quantity): # переопределили метод для дочернего класса
        self.health += quantity * 2
        other.health -= quantity * 2
    
    def add_many_up(self):
        self.up += 1
        self.up = min(self.up, self._Person4__max_up * 2) # почему дочерний класс так обращается? наверно не надо делать приватной

# p1 = Hero('archery', 'Сильвана', 'Эльф', 120)
# print(f'{p1.name = }, {p1.up = }, {p1.power = }')#p1.name = 'Сильвана', p1.up = 3, p1.power = 'archery'

p1 = Hero('archery', 'Сильвана', 'Эльф', 120)
p2 = Person4('Маг', 'Тролль')
print(f'{p1.health = }, {p2.health = }')#p1.health = 100, p2.health = 100

p1.change_health(p2, 10)
print(f'{p1.health = }, {p2.health = }')# p1.health = 120, p2.health = 80

p2.change_health(p1, 10)
print(f'{p1.health = }, {p2.health = }')# p1.health = 110, p2.health = 90

p1.add_many_up()
print(f'{p1.up = }') #p1.up = 4
# если у Hero нет метода, можно вызвать из родительского класса