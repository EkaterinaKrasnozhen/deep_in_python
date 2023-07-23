import unittest

class TestSample(unittest.TestCase):
    def setUp(self) -> None:
        with open('top_secret.txt', 'w', encoding='utf-8') as f:
            for i in range(10):
                f.write(f'{i:05}\n')
            # 00000
            # 00001
            # 00002
            # 00003
            # 00004
            # 00005
            # 00006
            # 00007
            # 00008
            # 00009

    def test_line(self):
        with open('top_secret.txt', 'r', encoding='utf-8') as f:
            for i, line in enumerate(f, start=1):
                pass
        self.assertEqual(i, 10)
        
    def test_first(self):
        with open('top_secret.txt', 'r', encoding='utf-8') as f:
            first = f.read(5)
            self.assertEqual(first, '00000')

    def tearDown(self) -> None: # независимо от того как были пройдет тесты делает то, что прописано после них
        from pathlib import Path
        Path('top_secret.txt').unlink() # удаляет, чистит


if __name__ == '__main__':
    unittest.main()