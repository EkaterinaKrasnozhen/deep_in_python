# * Создайте вручную кортеж содержащий элементы разных типов.
# * Получите из него словарь списков, где:
# ключ — тип элемента,
# значение — список элементов данного типа.

my_list = (9, True, "Heelo", "Bye", 11)
my_dic = {}
my_dic2 = {}
for item in my_list:
    my_dic.setdefault(type(item), []).append(item)
    my_dic2[type(item)] = my_dic2.get(type(item), []) + [item]
print(f'{my_dic},\n{my_dic2}')