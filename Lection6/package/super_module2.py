from random import randint
__all__ = ['func', '_secret']

SIZE = 100
_secret = 'qwerty' # секретная переменная
__top_secret = 'qweasd' #сверхсекретная

def func(a: int, b: int) ->str:
    z = f"в диапазоне от {a} до {b} получили = {randint(a,b)}"
    return z

