# Задание №1
# ✔ Пользователь вводит строку из четырёх
# или более целых чисел, разделённых символом “/”.
# Сформируйте словарь, где:
# ✔второе и третье число являются ключами.
# ✔первое число является значением для первого ключа.
# ✔четвертое и все возможные последующие числа
#  хранятся в кортеже как значения второго ключа

user_input = input('Значения через /: ')
a, b, c, *d = user_input.split('/')
my_dict2 = {b: a, c: tuple(d)}
print(my_dict2)#{'23': '1', '34': ('567', '0')}