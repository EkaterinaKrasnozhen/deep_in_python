# Задание №4
# Напишите для задачи 1 тесты pytest. Проверьте следующие
# варианты:
# возврат строки без изменений
# возврат строки с преобразованием регистра без потери
# символов
# возврат строки с удалением знаков пунктуации
# возврат строки с удалением букв других алфавитов
# возврат строки с учётом всех вышеперечисленных пунктов
# (кроме п. 1)

import pytest
from Task1 import del_all


def test_del_all_1():
    assert del_all('doctest pytest unitest') == 'doctest pytest unitest', 'NOT OK'

    
def test_del_all_2():
    assert del_all('Doctest Pytest Unitest') == 'doctest pytest unitest', 'NOT OK'


def test_del_all_3():
    assert del_all('doctest, pytest! unitest:') == 'doctest pytest unitest', 'NOT OK'


def test_del_all_4():
    assert del_all('doctest доктест pytest пайтест  unitest юнитест') == 'doctest  pytest   unitest ', 'NOT OK'


def test_del_all_5():
    assert del_all('Doctest! доктест, Pytest пайтест:  Unitest? юнитест.') == 'doctest  pytest   unitest ', 'NOT OK'

   
if __name__ == '__main__':
    pytest.main()