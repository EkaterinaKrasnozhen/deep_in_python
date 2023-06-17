list_1 = list()
list_2 = list((3.14, "Hello", True)) # вызов функции
list_3 = [] # список пустой
list_4 = [3.14, True, "Hello"]
# print(list_4[-1]) #Hello
# #append - добавить в конец
# list_4.append(list_2)
# print(list_4) #[3.14, True, 'Hello', [3.14, 'Hello', True]]
# #extend - пройтись и добавить
# c = [None]
# c.extend(list_2)
# print(c)# [None, 3.14, 'Hello', True] проходится по списку и добавляет каждый элемент отдельно

# #pop -удаляет последний() и по индексу(9)
# my_list = [1, 3, 4, 5]
# spam = my_list.pop() # 5
# print(spam, my_list) #5 [1, 3, 4]
# eggs = my_list.pop(1) # удаляем с индексом 1, сдвижение потом занимет время
# print(eggs, my_list) # 3 [1, 4]

# count
my_list = [1, 3, 4, 5, 1, 1, 1]
# spam_1 = my_list.count(1) # количество элементов 1 в списке my_list
# print(spam_1)#4

# index() - первое вхождение в списке
# spam = my_list.index(4) # ищем значение 4
# print(spam) #2 значение 4 под индексом 2 в списке spam_1
# eggs = my_list.index(5, spam+1, 10)# ищу значение 5, с индекса 3(spam = 2 + 1) и до индекса 10
# print(eggs)#3

#insert
# list1 = [2, 3, 5, 6]
# list1.insert(2, 555)# сначала указываем позицию, куда вставить - индекс 2, потом значение, которое нужно вставить
# print(list1) #[2, 3, 555, 5, 6]
# list1.insert(-1, 666)
# print(list1)#[2, 3, 555, 5, 666, 6] append работает быстрее

# #remove удалить по значению
# list2 = [1, 4, 5, 7]
# list2.remove(1)
# print(list2)#[4, 5, 7]

# sorted - не смешивать текст и числа
# list2 = [1, 5, 4, 7]
# sort_list = sorted(list2)
# print(list2, sort_list, sep='\n')#[1, 4, 5, 7]
# rev_list = sorted(list2, reverse=True) # в порядке убывающем
# print(rev_list)#[7, 5, 4, 1]

#sort и список и кортеж и множество
# list2 = [1, 5, 4, 7]
# list2.sort()# не создаем новый список, а работаем с текущим
# print(list2)#[1, 4, 5, 7]
# list2.sort(reverse=True)# в порядке убывающем
# print(list2)#[7, 5, 4, 1]

#разворот reversed
# list2 = [1, 5, 4, 7]
# res = list(reversed(list2))# надо все обернуть в list
# print(res)#[7, 4, 5, 1]

# list2.reverse()
# print(list2)#[7, 4, 5, 1]
# new_list = list2[::-1] # синт сахар срезов, срез от начала до конца в обратном порядке
# print(new_list)

# срезы
# list3 = [2, 4, 5, 6, 8, 10, 4]
# print(list3[2:7:2]) # старт индекс(вкл), стоп индекс(в срез не вкл), шаг, [5, 8, 4]
# print(list3[:7:2]) # если пропускаем первое значение = по умолчанию 0, [2, 5, 8, 4]
# print(list3[2::2]) # пропускаем второе значение = до конца списка, [5, 8, 4]
# print(list3[2:7:]) # шаг по умолчанию 1, каждый элемент, [5, 6, 8, 10, 4]
# print(list3[::-1])# с конца -1, [4, 10, 8, 6, 5, 4, 2]

#копирование
# list3 = [2, 4, 5, 6, 8, 10, 4]
# list4 = list3
# list3[2] = 555 # добавится в оба
# print(list3, list4) # [2, 4, 555, 6, 8, 10, 4] [2, 4, 555, 6, 8, 10, 4]

# list3 = [2, 4, 5, 6, 8, 10, 4]
# new_list = list3.copy()
# list3[2] = 555 # добавит только в оригинал
# print(list3, new_list) # [2, 4, 555, 6, 8, 10, 4] [2, 4, 5, 6, 8, 10, 4]

# matrix = [[1,2,3], [1,2,3], [3,5,6]]
# new_matr = matrix.copy()
# matrix[0][1] = 555 # при 2ой вложенности изменения будут в обоих 
# print(matrix, new_matr) # [[1, 555, 3], [1, 2, 3], [3, 5, 6]] [[1, 555, 3], [1, 2, 3], [3, 5, 6]]
# import copy

# matrix = [[1,2,3], [1,2,3], [3,5,6]]
# new_m = copy.deepcopy(matrix) # для любой вложенности
# matrix[0][1] = 555
# print(matrix, new_m) #[[1, 555, 3], [1, 2, 3], [3, 5, 6]] [[1, 2, 3], [1, 2, 3], [3, 5, 6]]
# # на срезы и копии тратим оперативную память

# # len() замеряет поверхностную длину
# list3 = [2, 4, 5, 6, 8, 10, 4]
# matrix = [[1,2,3,5,7], [1,2,3], [3,5,6]]
# print(len(list3))#7 элементов
# print(len(matrix))#3 - считает первый уровнень вложенности
# print(len(matrix[0])) #5 для конкретного элемента матрицы

# str строки
# txt = 'Hello Kate'
# # print(txt[1]) #e
# # print(txt[2::3]) #l t
# # new_txt = txt.replace('l', 'L', 2) # вместо какого сделать какой, количство замен (есди ничегог -то все заменить )
# # print(new_txt, txt) #HeLLo Kate Hello Kate
# print(txt.count('l')) #2
# print(txt.index('K')) #6 первое вхождение буквы
# print(txt.find("z")) # -1, похожа на index() но если такой нет - вернет -1
# print(txt[::-1])#etaK olleH

#форматирование строк
# name ="Kate"
# age = 18
# text = "Меня зовут %s и мне %d лет" %(name, age) # d - число, s - строки, старое форматирование
# print(text) # Меня зовут Kate и мне 18 лет
# name ="Kate"
# age = 18
# # text = "Меня зовут {} и мне {} лет".format(name, age)
# # print(text)
# text = f"Меня зовут {name} и мне {age} лет"
# print(text)
# print(f'{{скобки}}') # если вывести {}

# pi = 3.1415
# print(f' число пи с точностью 2 знака: {pi: .2f}')

# data = [2334, 45677777777777777776, 4456777, 3435]
# for item in data:
#     print(f'{item:>10}') #отсуп вправо 10 сим, < - влеов, ^ по центру
    
# num = 2 * pi * data[0]
# print(f'{num = :_}')#num  =  14_664.522

#строковые методы

#split
# link = "www./habr.ru/splash"
# user = link.split('/')
# print(user)# ['www.', 'habr.ru', 'splash']
# a, b, c = input("введите через пробел 3 цифры").split()
# print(a,b,c)

# a, b, c, *_ = input("введите через пробел 3 цифры").split() # *_ все что н войдет в первые три
# print(a, b, c, *_)

#join
# data = ['www.', 'habr.ru', 'splash']
# url = "/".join(data) #копирует и разделяет все элементы /, только между элементами, вначале и в конце нет
# print(url) #www./habr.ru/splash

#upper, lower, title
# text = 'wwW.' 'haBr.ru' 'splash'
# print(text.upper()) # WWW.HABR.RUSPLASH
# print(text.lower()) #www.habr.rusplash
# print(text.title()) #Www.Habr.Rusplash
# print(text.capitalize()) # Www.habr.rusplash - заглавная только 1 буквы строки

# # startswith endswith
# text = "Однажды в студеную зимнюю пору"
# print(text.startswith("Однажды")) #True
# print(text.endswith('зимнюю', 0, -5))  #True граница до -5 индекса с конца (каждый символ считается)

# кортеж - неизменяемый список 
# b = ()
# d = tuple(range(3))
# c2 = (1, 2, 3)
# print(d)
# f(a,d,c) - передаем 3 аргумента
#f((a,b,c)) - передаем один кортеж с 3 элементами

#dict словари пара ключ и значение, ключ неизменяемое значение. не могут повторяться
a = {'one': 42, 'two': 3.14}
b = dict(one= 42, two= 3.14)
#print(a, b) #{'one': 42, 'two': 3.14} {'one': 42, 'two': 3.14}
c = dict([('one', 54), ('two', 66)])
#print(c) #{'one': 54, 'two': 66}
x = 10
c['one'] = x
# print(c) #{'one': 10, 'two': 66}

# TEN = 'two'
# print(c[TEN])#66

# print(c.get("two")) # 66
# print(c.get("ten")) #None
# print(c.get("ten", 10)) #10 не найден, но передали значение по умолчанию и вернется 10

# my_dict = c.setdefault('five')
# print(f'{my_dict=}\t{c=}') # None    {'one': 10, 'two': 66, 'five': None}
# eggs = c.setdefault('six', 6)
# print(f'{eggs=}\t{c=}') #6       {'one': 10, 'two': 66, 'five': None, 'six': 6}
# twos = c.setdefault('two')
# print(f'{twos=}\t{c=}')#66      {'one': 10, 'two': 66, 'five': None, 'six': 6}
# nothing = c.setdefault('one', 1000)
# print(f'{nothing=}\t{c}') # nothing=10      {'one': 10, 'two': 66, 'five': None, 'six': 6} не ихменится, так как уже было значение, меняет если не было

# print(c.keys())#dict_keys(['one', 'two', 'five', 'six']) ключи в порядке добавления
# for key in c.keys(): # или просто in c
#     print(key) #one two five six обычно так делают
    
# for value in c.values():
#     print(value) # 10 66 None 6
    
# for key, value in c.items():
#     print(f'{key=}{value=}') #key='one'value=10

# spam = c.popitem() # удвлет посл пару ключ/значение
# print(spam, c)# ('two', 66) {'one': 10}

# spam = c.pop("one") # без кюча ошибка
# print(f'{spam=}{c=}')#spam=10 c={'two': 66}

# c.update(dict(six=6))
# print(c)#{'one': 10, 'two': 66, 'six': 6}
# c.update(dict([('one', 6)])) # {'one': 6, 'two': 66, 'six': 6}
# print(c)
# new_dict = c | {'ten': 54} 
# print(new_dict) # {'one': 6, 'two': 66, 'six': 6, 'ten': 54}
# my_dic = {'six': 1,
#           'seven': 5,
#           'tenn': 7, #лучше ставить запятые даже после полсднего, при добавлении не будет ошибки
#           }

# set frozenset
my_set = {1,2,3,2,5,6} #изменяемое множество, только уникальные эелементы 1, 2, 3, 5, 6

my_f_set = frozenset((1,2,3,2 ,4,5)) #неизменяемое множество 1, 2, 3, 4, 5
#print(my_set, my_f_set)
my_set.add(9)#добавляем по одному
print(my_set)#{1, 2, 3, 5, 6, 9}
my_set.add((11,10))# добвляет так воспринимает кортеж как один эелемент
print(my_set)#{1, 2, 3, 5, 6, (11, 10), 9}
my_set.remove(1)
print(my_set)#{2, 3, 5, 6, (11, 10), 9}
my_set.discard(15) #не вызыввает ошиюку при попытке удалить несуществующий элемент

# #intersection
# other_set = {13,2,18,3}
# new_set = my_set.intersection(other_set)#ищет пересечения элементов
# print(new_set)#{2, 3}
# new_set2 = my_set & other_set
# print(new_set2) # {2, 3}

# #union
# new_set_union = my_set.union(other_set)
# print(new_set_union)#{2, 3, 5, 6, (11, 10), 9, 13, 18} повторяющихся нет, объединили
# new_set_un = my_set | other_set
# print(new_set_un)#{2, 3, 5, 6, (11, 10), 9, 13, 18}

# #difference вычитание
# set_disc = my_set.difference(other_set)
# print(set_disc)#{(11, 10), 9, 5, 6} только те значение, кторые уникальны для первого множества, если есть эл в первом и втором множестве
# # он убирается, а если есть те, которые только во 2 множестве - они не учитываются
# new_diff = my_set - other_set
# print(new_diff)#{(11, 10), 9, 5, 6}

#вхождение in
print(2 in my_set)#True
