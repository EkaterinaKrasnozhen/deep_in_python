# Задание №5
# ✔ Напишите программу, которая выводит
# на экран числа от 1 до 100.
# ✔ При этом вместо чисел, кратных трем,
# программа должна выводить слово «Fizz»
# ✔ Вместо чисел, кратных пяти — слово «Buzz».
# ✔ Если число кратно и 3, и 5, то программа
# должна выводить слово «FizzBuzz».
# ✔ *Превратите решение в генераторное выражение.


def gen_():
    for i in range(1, 101):
        if i % 3 == 0:
            yield "Fizz"
        elif i % 5 == 0:
            yield "Buzz"
        elif i % 15 == 0:
            yield "FizzBuzz"
        else:
            yield i
        
        
res1 = gen_()
print(*res1)
