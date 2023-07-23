import doctest
import unittest
import prime

def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(prime)) # берет из файла prime.py
    tests.addTests(doctest.DocFileSuite('prime.md'))
    return tests


if __name__ == '__main__':
    unittest.main(verbosity=True)
