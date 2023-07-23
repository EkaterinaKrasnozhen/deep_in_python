# Задание №5
# На семинарах по ООП был создан класс прямоугольник
# хранящий длину и ширину, а также вычисляющую периметр,
# площадь и позволяющий складывать и вычитать
# прямоугольники беря за основу периметр.
# Напишите 3-7 тестов unittest для данного класса.
import unittest
from Rect import RectangleNEW


class TestSample(unittest.TestCase):
    def setUp(self) -> None:
        self.rect = RectangleNEW(3, 4)
        self.rect2 = RectangleNEW(4, 5)
    
    def test_first(self):
        first = self.rect.perimeter()
        self.assertEqual(first, 14, msg='not ok')
        
    def test_second(self):
        second = self.rect.s()
        self.assertEqual(second, 12)
        
    def test_thirth(self):
        thirth = self.rect == self.rect2
        self.assertEqual(thirth, False)
            

if __name__ == '__main__':
    unittest.main()