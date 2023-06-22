# Функция получает на вход список чисел.
# Отсортируйте список по убыванию суммы цифр

my_list = [11, 45, 13]
def get_sum(num):
    return sum(map(int, str(num)))

print(sorted(my_list, key=get_sum, reverse=True)) # [45, 13, 11]

def get_dict(lst):
    return dict(sorted(zip(map(get_sum, lst), lst), key=lambda x: x[0], reverse=True)) # {9: 45, 4: 13, 2: 11}

print(get_dict(my_list)) 
            
