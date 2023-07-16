# Задание №1
# Создайте класс-функцию, который считает факториал числа при
# вызове экземпляра.
# Экземпляр должен запоминать последние k значений.
# Параметр k передаётся при создании экземпляра.
# Добавьте метод для просмотра ранее вызываемых значений и
# их факториалов.

# Задание №2
# Доработаем задачу 1.
# Создайте менеджер контекста, который при выходе
# сохраняет значения в JSON файл.


from math import factorial
from collections import defaultdict
import json

class Factorial_:
    def __init__(self):
        self.storage = {}
         
    def __call__(self, k):
        for i in range(1, k+1):
            self.storage.setdefault(i, factorial(i))
        return f'К значению {i} добавлен результат функции факторил {factorial(i)}'
    
    def __str__(self):
        txt = '\n'.join((f'{k}: {v}' for k, v in self.storage.items()))
        return txt

    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        with open ('result.json', 'a', encoding='utf-8') as f:
            json.dump(self.storage, f, ensure_ascii=False)
            
    
fact = Factorial_()
print(fact(6))
print(fact.storage)
with fact:
    print()
        
