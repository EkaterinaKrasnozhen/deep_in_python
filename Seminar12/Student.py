# Создайте класс студента. 
# Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв. 
# Названия предметов должны загружаться из файла CSV при создании экземпляра. 
# Другие предметы в экземпляре недопустимы. 
# Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100). 
# Также экземпляр должен сообщать средний балл по тестам для каждого 
# предмета и по оценкам всех предметов вместе взятых.
import csv
from random import randint as rnd
import Cvs_creator

class Student:
    def __init__(self, id_, name, middle_name, surname):
        self.name = name
        self.middle_name = middle_name
        self.surname = surname
        self.id_ = id_
        data = Cvs_creator.read_csv('studen2.csv')
        self.student_data = data[str(id_)]
        
    def get_score(self, csv_file):
        pass


student1 = Student(1, 'Kate', 'Leonidovna', 'Kras')
print(student1.student_data)
