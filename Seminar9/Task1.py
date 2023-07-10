# Задание №1
# Создайте функцию-замыкание, которая принимает два целых числа:
# от 1 до 100 для загадывания,
# от 1 до 10 для количества попыток
# Функция возвращает функцию, которая через консоль просит угадать загаданное число за указанное число попыток. 


def counter(num, try_num):# замкнули num и try_num а def try_() внутри запрашивает ответ и работает
    def try_():
        count = 0
        MIN = 1
        MAX = 100
        print(f'Отгадайте число от {MIN} до {MAX} за {try_num} раз')
        while count < try_num: 
            user_num = int(input("Введите число от 1 до 100: "))
            if num == user_num:
                print('Вы отгадали')
                break   
            else:
                count += 1
                print('Вы не угадали')
        else: 
            print('число попыток исчерапно, до свидания') 
    return try_

          
if __name__ == '__main__':
    res = counter(5, 2)
    res()