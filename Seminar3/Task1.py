# Вручную создайте список с целыми числами, которые повторяются. 
# Получите новый список, который содержит уникальные (без повтора) 
# элементы исходного списка
# * Подготовьте два решения, короткое и длинное, которое
# не использует другие коллекции помимо списков

my_set = [1,2,3,2,5,6]
new_set = set(my_set)
new_set3 = [*set(my_set)] # [1, 2, 3, 5, 6]
print(new_set) #{1, 2, 3, 5, 6}
print(new_set3)
new_set2 = []
for item in my_set:
    if item not in new_set2:
        new_set2.append(item)#[1, 2, 3, 5, 6]
    
print(new_set2)