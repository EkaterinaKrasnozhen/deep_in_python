# Задание №4
# Создайте класс Сотрудник.
# Воспользуйтесь классом человека из прошлого задания.
# У сотрудника должен быть:
# ○ шестизначный идентификационный номер
# ○ уровень доступа вычисляемый как остаток от деления
# суммы цифр id на семь
from random import randint
from Human import Human



class Staff(Human):
    MIN_ID = 6
    
    def __init__(self, id_num, *args, **kwargs):
        if len(str(id_num)) != self.MIN_ID:
            id_num = randint(100000, 999999)
        self.id_num = id_num
        super().__init__(*args, **kwargs)
        self.grade = self.get_grade()
  
    def get_grade(self):
        delimeter = 7
        return sum(map(int, str(self.id_num))) % delimeter
        
    
pers = Staff(5545, 'Иван', 'Иванович', 'Иванов', 39)
print(pers.grade, pers.id_num)

