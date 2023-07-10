class Person:
    max_up = 3
    
    
# p1 = Person()
# p2 = Person()
# print(f'{Person.max_up = }, {p1.max_up = }, {p2.max_up = }') #Person.max_up = 3, p1.max_up = 3, p2.max_up = 3

# p1.max_up = 12
# print(f'{Person.max_up = }, {p1.max_up = }, {p2.max_up = }') #Person.max_up = 3, p1.max_up = 12, p2.max_up = 3  

# Person.max_up = 42
# print(f'{Person.max_up = }, {p1.max_up = }, {p2.max_up = }') #Person.max_up = 42, p1.max_up = 12, p2.max_up = 42

# # p1.health = 100# присвоили атрибут конкретному экз класса, не всему классу
# # print(p1.health) # 100 

# # хранениео похоже на словари
# p1.level = 1
# p1.health = 100
# dict_p1 = {}
# dict_p1['level'] = 1
# dict_p1['health'] = 100
# print(f'{p1.health = }') # p1.health = 100
# print(f'{dict_p1["health"] = }') # dict_p1["health"] = 100

# def __init__(self): # не явл зарезервированным словом, но всегда используют. параметры метода __init__ попадают в экз
#     self.level = 1 # обащения к атрибутам экземпляра
#     self.health = 100


    def __init__(self, name, race='unknown'):
        self.name = name
        self.race = race
        self.level = 1
        self.health = 100
        
    def level_up(self):
        self.level += 1
        
    def change_health(self, other, quantity): # один получает здоровье, другой уменьшает
        self.health += quantity
        other.health -= quantity

p1 = Person('Сильвана', 'Эльф')
p2 = Person('Иван', 'Человек')
p3 = Person('Грогу')
print(f'{p1.name = }, {p1.race = }')
print(f'{p2.name = }, {p2.race = }')
print(f'{p3.name = }, {p3.race = }')

#p1.name = 'Сильвана', p1.race = 'Эльф'
#p2.name = 'Иван', p2.race = 'Человек
#p3.name = 'Грогу', p3.race = 'unknown'

p3.level_up()
print(f'{p1.level=} {p3.level=}') #p1.level=1 p3.level=2

print(f'{p1.health = }, {p2.health = }, {p3.health = }') #p1.health = 100, p2.health = 100, p3.health = 100
p1.change_health(p2, 10)
print(f'{p1.health = }, {p2.health = }, {p3.health = }') #p1.health = 110, p2.health = 90, p3.health = 100

