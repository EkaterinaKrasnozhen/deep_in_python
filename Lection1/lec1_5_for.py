data = [0,1,2,4,5,7,6]
for item in data:
    print(item, end=',')
    
for _ in data: #если не нужна переменная, чтобы не сломалось
    print('item', end=',')
    
num = 10
for i in range(0, num, 2): #0 -старт(включительно), num -конец (не включительно), 2 - шаг
    print(i)
    
animals = ['cat', 'dog', 'elefant']
for i, animal in enumerate(animals, start=1): #первое -список, второе = ключевое значение с котрого начать
    print(i, animal)