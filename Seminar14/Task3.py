# Напишите для задачи 1 тесты unittest. Проверьте
# следующие варианты:
# возврат строки без изменений
# возврат строки с преобразованием регистра без потери
# символов
# возврат строки с удалением знаков пунктуации
# возврат строки с удалением букв других алфавитов
# возврат строки с учётом всех вышеперечисленных пунктов
# (кроме п. 1)
import unittest
from Task1 import del_all


class TestSample(unittest.TestCase):
    def test_first(self):
        first = del_all('doctest pytest unitest')
        self.assertEqual(first, 'doctest pytest unitest', msg='not ok')
        
    def test_second(self):
        second = del_all('Doctest Pytest Unitest')
        self.assertEqual(second, 'doctest pytest unitest')
        
    def test_thirth(self):
        thirth = del_all('doctest, pytest! unitest:')
        self.assertEqual(thirth, 'doctest pytest unitest')
        
    def test_fourth(self):
        fourth = del_all('doctest доктест pytest пайтест  unitest юнитест')
        self.assertEqual(fourth, 'doctest  pytest   unitest ')
        
    def test_fifrth(self):
        fifth = del_all('Doctest! доктест, Pytest пайтест:  Unitest? юнитест.')
        self.assertEqual(fifth, 'doctest  pytest   unitest ')
    

if __name__ == '__main__':
    unittest.main()