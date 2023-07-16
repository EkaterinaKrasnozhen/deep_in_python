# Задание №3
# Создайте класс-генератор.
# Экземпляр класса должен генерировать факториал числа в
# диапазоне от start до stop с шагом step.
# Если переданы два параметра, считаем step=1.
# Если передан один параметр, также считаем start=1.

from math import factorial

class MyGenFact:
    def __init__(self, stop, start=1, step=1):
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        return self
    
    def __next__(self):
        while self.start < self.stop + 1:
            num = factorial(self.start)
            self.start += self.step
            return num    
        raise StopIteration


fact = MyGenFact(6, 1, 2)
for num in fact: 
    print(num)