import random as rnd

print(f'{rnd.random()=}') #rnd.random()=0.8768220456693637б от 0 до 1 искл
rnd.seed() # лучше не передавать точные значения, чтобы не получить сопадений дальше
state = rnd.getstate() # большой набор чисел
#print(f'{state=}')
print(f'{rnd.random()=}')

START = -100
STOP = 1000
STEP = 10
data = [2, 4, 8, 54, 77]
# print(f'{rnd.randint(START, STOP)=}') #rnd.randint(START, STOP)=245
# print(f'{rnd.uniform(START, STOP)=}') #rnd.uniform(START, STOP)=5.201904698130662 float
# print(f'{rnd.choice(data)=}')#rnd.choice(data)=8
# print(f'{rnd.randrange(START, STOP, STEP)=}')#rnd.randrange(START, STOP, STEP)=770

rnd.shuffle(data)
print(f'{data=}')#data=[77, 54, 2, 4, 8]
print(f'{rnd.sample(data, 3)=}')#rnd.sample(data, 3)=[2, 8, 77]
print(f'{rnd.sample(data, 3, counts=[1, 1, 1, 1, 100])=}') #rnd.sample(data, 3, counts=[1, 1, 1, 1, 100])=[54, 54, 54] верни список где 1ый элемент содержится 1 раз, 2ой 1 раз.. 5ый сто раз


