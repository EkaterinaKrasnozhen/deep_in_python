class User():
    def __init__(self, name: str):
        self.name = name
        print(f'Создал {self.name = }')
    
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        print(f'Создал класс {cls}')
        return instance
    
print('Создаём первый раз')
u_1 = User('Спенглер')
# Создаём первый раз
# Создал класс <class '__main__.User'>
# Создал self.name = 'Спенглер'

print('Создаём второй раз')
u_2 = User('Венкман')
# Создаём второй раз
# Создал класс <class '__main__.User'>
# Создал self.name = 'Венкман' 

print('Создаём третий раз')
u_3 = User(name='Стэнц')
# Создаём третий раз
# Создал класс <class '__main__.User'>
# Создал self.name = 'Стэнц'