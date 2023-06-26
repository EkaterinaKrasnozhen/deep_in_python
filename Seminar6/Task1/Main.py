import Func

start_, stop_, num_count = (input('Введите начало диапоза, конец диапазон, количество попыток через пробел: ')).split(' ')
#print(f'{start_=} {stop_=} {num_count=}')

some_num = Func.generate_rnd(int(start_), int(stop_))
print(some_num)

print(f'Угадайте число в диапазоне {start_} {stop_}')
res = Func.try_get(some_num, int(num_count))
print(res)
