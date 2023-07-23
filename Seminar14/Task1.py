# Задание №1
# Создайте функцию, которая удаляет из текста все символы
# кроме букв латинского алфавита и пробелов.
# Возвращается строка в нижнем регистре.

# Задание №2
# Напишите для задачи 1 тесты doctest. Проверьте
# следующие варианты:
# возврат строки без изменений
# возврат строки с преобразованием регистра без потери
# символов
# возврат строки с удалением знаков пунктуации
# возврат строки с удалением букв других алфавитов
# возврат строки с учётом всех вышеперечисленных пунктов
# (кроме п. 1)
from string import ascii_letters


def del_all(text: str) -> str:
    """Возвращает строку в нижнем регистре, содержащую только символы латинского алфавита и пробелы.
    >>> del_all('doctest pytest unitest') 
    'doctest pytest unitest'
    >>> del_all('Doctest Pytest Unitest') 
    'doctest pytest unitest'
    >>> del_all('doctest, pytest! unitest:') 
    'doctest pytest unitest'
    >>> del_all('doctest доктест pytest пайтест  unitest юнитест') 
    'doctest  pytest   unitest '
    >>> del_all('Doctest! доктест, Pytest пайтест:  Unitest? юнитест.') 
    'doctest  pytest   unitest '
    """
    new_text = ''.join(c for c in text if c in ascii_letters or c == ' ').lower()
    return new_text


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
    