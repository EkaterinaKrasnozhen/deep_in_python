# Создайте модуль с функцией внутри.
# Функция принимает на вход три целых числа: нижнюю и верхнюю границу и количество попыток.
# Внутри генерируется случайное число в указанных границах и пользователь должен угадать его за заданное число попыток.
# Функция выводит подсказки “больше” и “меньше”.
# Если число угадано, возвращается истина, а если попытки исчерпаны - ложь.
import random as rnd

def generate_rnd(start, stop):
    num = rnd.randint(start, stop)
    return num



def try_get(num, count):
    while count :
        user_num = int(input("Введите число: "))
        if num < user_num:
            count -= 1
            print("ваше число больше загаданного, осталось попыток: ", count)

        elif num > user_num:
            count -=1
            print("ваше число меньше загаданного, осталось попыток: ", count)

        else:
            return True


    else:
        return False
        

if __name__ == '__main__':
    print(f'{generate_rnd(2, 10)=}')
    print(f'{count_(0)}')
