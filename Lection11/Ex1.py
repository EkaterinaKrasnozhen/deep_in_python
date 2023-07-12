class User():
    def __init__(self, name: str, equipment: list = None):
        self.name = name
        self.equipment = equipment if equipment is not None else []
        self.life = 3
        # принтим только в учебных целях, а не для реальных задач
        print(f'Создал {self} со свойствами:\n'
            f'{self.name = },\t{self.equipment = },\t{self.life= }')
        
print('Создаём первый раз')
u_1 = User('Спенглер')
# Создаём первый раз
# Создал <__main__.User object at 0x0000019A64C5BF70> со свойствами:
# self.name = 'Спенглер', self.equipment = [],    self.life= 3

print('Создаём второй раз')
u_2 = User('Венкман', ['протонный ускоритель', 'ловушка'])
# Создаём второй раз
# Создал <__main__.User object at 0x0000019A64C5BF10> со свойствами:
# self.name = 'Венкман',  self.equipment = ['протонный ускоритель', 'ловушка'],   self.life= 3

print('Создаём третий раз')
u_3 = User(equipment=['ловушка', 'прибор ночного видения'], name='Стэнц')
#Создаём третий раз
#Создал <__main__.User object at 0x0000019A64C5BEB0> со свойствами:
#self.name = 'Стэнц',    self.equipment = ['ловушка', 'прибор ночного видения'], self.life= 3