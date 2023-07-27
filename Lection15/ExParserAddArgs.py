import argparse


def quadratic_equations(a, b, c):
    d = b ** 2 - 4 * a * c
    if d > 0:
        return (-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 * a)
    if d == 0:
        return -b / (2 * a)
    return None
# python ExParserAddArgs.py 2 -12 10        (5.0, 1.0)
# python ExParserAddArgs.py -h

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Solving quadratic equations')
    parser.add_argument('param', metavar='a b c', type=float,
    nargs=3, help='enter a b c separated by a space') # nargs3  a b c a b c a b c в след примере заменили на 3 строки
    # при вызове справки будем видеть abc
    args = parser.parse_args()
    print(quadratic_equations(*args.param))
    
