from random import randint
__all__ = ['func', '_secret']

SIZE = 100
_secret = 'qwerty' # секретная переменная
__top_secret = 'qweasd' #сверхсекретная

def func(a: int, b: int) ->str:
    z = f"в диапазоне от {a} до {b} получили = {randint(a,b)}"
    return z

#print(f'{func(2,5)=}') # в main будет func(2,5)='в диапазоне от 2 до 5 получили = 2'

if __name__ =='__main__': # есть так указать, то тестовые принты не придут в запуск в другом файле
    print(f'{func(3, 5)=}')