# Задание №7
# ✔ Создайте функцию-генератор.
# ✔ Функция генерирует N простых чисел,
# начиная с числа 2.
# ✔ Для проверки числа на простоту используйте
# правило: «число является простым, если делится
# нацело только на единицу и на себя».

n = 11
START = 3
def simple_(num):
    if num % 2 == 0 and num != 2:
        return False
    else:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        else:
            return True

    
    
def gen_simple_(n):
    count = 0
    yield 2
    number = 3
    while count < n:
        if simple_(number):
            yield number
            count += 1
        number += 2        
res = gen_simple_(15)
print(*res)
                
        
