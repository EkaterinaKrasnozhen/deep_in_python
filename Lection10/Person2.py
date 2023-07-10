class Person2:
    max_up = 3
    _max_level = 80# защищенный атрибут, не влиять
    
    def __init__(self, name, race='unknown', speed=100):
        self.name = name
        self.race = race
        self.level = 1
        self.health = 100
        self._speed = speed # тоже защищенная
    
    def _check_level(self): #инкасуляция, защищенный метод
        return self.level < self._max_level # внутри класса можо обращаться к защищн=еным переменным
    
    def level_up(self):
        if self._check_level():
            self.level += 1

    def change_health(self, other, quantity):
        self.health += quantity
        other.health -= quantity


p1 = Person2('Сильвана', 'Эльф', 120)
p2 = Person2('Иван', 'Человек')
p3 = Person2('Грогу', speed=60)
print(f'{p1._max_level = }')#p1._max_level = 80 неправильно обращаться черз ._ к защищенным, но python разрешает
print(f'{p2._speed = }')#p2._speed = 100

p2._speed = 150
print(f'{p2._speed = }')#p2._speed = 150

p3.level_up()
print(f'{p3.level = }')#p3.level = 2

p3.level = 80
p3.level_up() # максимальный уже 80
print(f'{p3.level = }')#p3.level = 80