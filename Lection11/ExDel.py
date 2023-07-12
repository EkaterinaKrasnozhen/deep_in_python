import sys
class User:
    def __init__(self, name: str):
        self.name = name
        print(f'Создал {self.name = }')

    def __del__(self):
        print(f'Удаление экземпляра {self.name}')

u_1 = User('Спенглер')
print(sys.getrefcount(u_1))#2  метод делает свою ссылку и поэтому два

u_2 = u_1
print(sys.getrefcount(u_1), sys.getrefcount(u_2)) # 3 3

del u_1
print(sys.getrefcount(u_2))#2
print('Завершение работы')#Завершение работы
#Удаление экземпляра Спенглер - пайтон дошел до конца и вывел в конце