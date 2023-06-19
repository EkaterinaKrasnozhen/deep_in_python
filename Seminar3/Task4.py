#  Создайте вручную список с повторяющимися элементами.
# * Удалите из него все элементы, которые встречаются дважды.

my_list = [1, 3, 3, 3, 1, 555, 7, 7, 55]
# for item in my_list:
#     if my_list.count(item) == 2:
#         spam = item
#         my_list.remove(item)
#         find = my_list.index(spam)
#         my_list.remove(my_list[find])

# print(my_list) #[3, 3, 3, 555, 55]

for val in my_list:
    if my_list.count(val) == 2:
        for _ in range(2):
            my_list.remove(val)
            
print(my_list) # [3, 3, 3, 555, 55]
