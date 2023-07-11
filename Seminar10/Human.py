# Напишите класс для хранения информации о человеке: 
#     ФИО, возраст и т.п. на ваш выбор.
# У класса должны быть методы birthday для увеличения возраста на год, 
# full_name для вывода полного ФИО и т.п. на ваш выбор.
# Cвойство возраст должно быть недоступно для прямого обращения, 
# но возможность получить текущий возраст должна присутствовать.

class Human():
    def __init__(self, name, middle_name, surname, age):
       self.name = name
       self.middle_name = middle_name
       self.surname = surname
       self.__age = age
       
    def full_name(self):
        return str(self.surname +' ' + self.name +' ' + self.middle_name)
    
    def get_age(self):
        return self.__age
    
    def plus_year(self):
        self.__age += 1
        return self.__age
    

if __name__ == '__main__':
    pers = Human('Иван', 'Иванович', 'Иванов', 39)
    print(pers.full_name())
    print(pers.get_age())
    print(pers.plus_year())
    print(pers.plus_year())