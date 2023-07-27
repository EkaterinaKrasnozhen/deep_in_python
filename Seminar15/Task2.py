# Задание №2
# На семинаре про декораторы был создан логирующий
# декоратор. Он сохранял аргументы функции и результат её
# работы в файл.
# Напишите аналогичный декоратор, но внутри используйте
# модуль logging.
# Задание №3
# Доработаем задачу 2.
# Сохраняйте в лог файл раздельно:
# ○ уровень логирования,
# ○ дату события,
# ○ имя функции (не декоратора),
# ○ аргументы вызова,
# ○ результат.


from typing import Callable
import logging


FORMAT = '{levelname:<8} - {asctime}. {msg}' 
logging.basicConfig(format=FORMAT, style='{', filename='logging2.log.', filemode='a', encoding='utf-8', level=logging.INFO)
logger = logging.getLogger(__name__)    
    
def cache_(func: Callable):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            logger.info(f'функция {func.__name__}, аргументы {args=}, результат {result=}')
            return result
        except ZeroDivisionError:
            logger.error('ошибка деления на 0')
    return wrapper

    
@cache_
def division(a, b):
    return a/b


if __name__ ==  '__main__':
    division(2, 1)