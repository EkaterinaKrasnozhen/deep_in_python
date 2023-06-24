# a = 3
# b = 40
# a, b = b, a
# print(a, b) #40 3

# a,b,c = input('3 симовла') # только 3 элемента и без пробелов
# print(a, b, c)

# * только одну переменную
data = [1, 2, 3, 4, 5, 6]
# a, b, c, *d = data
# print(a,b,c,d)#1 2 3 [4, 5, 6]
a, b, *c, d = data
print(a,b,c,d)#1 2 [3, 4, 5] 6

link = 'http://doc.lib.org/3/flag/progrannibg.html'
prefix, *_, suffix = link.split('/')
print(prefix, suffix) # http: progrannibg.html, *_ значит не нужно выбросить

print(*data, sep='\t')# 1       2       3       4       5       6, * распаковка короткая запись for

# iter() возвращает объект итератор
list_iter = iter(data) # пройтись один раз
#print(*list_iter)

# next() работает последовательно со значениями итератора
print(next(list_iter, 42)) #1 когда закончится - будет по default 42 вместо исключения
data = {'один': 1, 'два': 2}
x = iter(data.items())
#print(*x)#('один', 1) ('два', 2)
y = next(x)
print(y)#('один', 1)
z = next(iter(y))
print(z)#один

#генераторы, получают данные и генерируют последовательности
a = range(0,10,2) # от 0 до 10 с шагом 2

#генераторные выражения, () будет генератор
my_gen = (chr(i) for i in range(97,123))
#print(*my_gen)# a b c d e f g h i j k l m n o p q r s t u v w x y z
for char in my_gen:
    print(char)
    
x = [1, 3, 34, 56 ,7, 123]
y = [1, 3, 55, 67, 87, 90]
print(f'{len(x)=} {len(y)=}') # len(x)=6 len(y)=6
mult = (i +j for i in x if i % 2 !=0 for j in y if j != 1)# каждый элемент i складываем с каждым подълдящим j, квадратично
# если не нужны все элементы сразу, можно перебрать их последовательно - генератор ()
res = list(mult)
print(f'{len(res)=} {res}') #len(res)=20 [4, 56, 68, 88, 91, 6, 58, 70, 90, 93, 10, 62, 74, 94, 97, 126, 178, 190, 210, 213]

#list copmrehensions, [], когда хотим получить все элементы сразу []
res = [item for item in x if item %2 == 0] # до 120 символов на строку
print(res) #[34, 56]

# словари{key: value} и множества(set) {1,2,2} через генераторы
res_set = {i+j for i in x if i % 2 != 0 for j in y if j != 1}
print(res_set)#{4, 6, 10, 178, 56, 58, 190, 62, 68, 70, 74, 210, 213, 88, 90, 91, 93, 94, 97, 126} # только уникальные

res_dict = {i: chr(i) for i in range(97, 100)}
print(res_dict)#{97: 'a', 98: 'b', 99: 'c'}
for number, char in res_dict.items():
    print(f'{number} = {char}') # 97 = a ...
    
#пишем генераторы, yield

def factorial(n):
    number = 1
    res = []
    for i in range(1, n+1):
        number *= i
        res.append(number)
    return res

def factorial2(n):
    number = 1
    for i in range(1, n+1):
        number *= i
        yield number

for i, num in enumerate(factorial(5), start=1):
    print(f'{i}! = {num}') # 1! = 1, 2! =2, 3! = 6..
    
# for i, num in enumerate(factorial2(5), start=1):
#     print(f'{i}! = {num}')

my_iter = iter(factorial2(4))
#print(*my_iter)# 1 2 6 24
print(next(my_iter)) #1
print(next(my_iter)) # 2
# в конце StopIterator, можно второй параметр по умочанию, когда заокнчится (my_iter, 42)