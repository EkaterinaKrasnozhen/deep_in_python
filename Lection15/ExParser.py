import argparse
parser = argparse.ArgumentParser(prog='average',
                                description='My first argument parser', 
                                epilog='Returns the arithmetic mean')
parser.add_argument('numbers', metavar='N', type=float, nargs='*', help='press some numbers')
args = parser.parse_args() # аргументы простанства Namespace
print(f'Получили экземпляр Namespace: {args = }')
print(f'У Namespace работает точечная нотация: {args.numbers =}')# прямое обращение к списку
print(f'Объекты внутри могут быть любыми: {args.numbers[1] = }')

# python ExParser.py --help

# python ExParser.py 4 3.14 73
# Получили экземпляр Namespace: args = Namespace(numbers=[4.0, 3.14, 73.0])
# У Namespace работает точечная нотация: args.numbers =[4.0, 3.14, 73.0]
# Объекты внутри могут быть любыми: args.numbers[1] = 3.14
