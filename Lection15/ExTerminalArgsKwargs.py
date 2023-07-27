import argparse

parser = argparse.ArgumentParser(description='My first argument parser')
parser.add_argument('numbers', metavar='N', type=float, nargs='*', help='press some numbers') # float будет .00, nargs - поместить все в [], metavar - то что будет выводиться в справке --help
args = parser.parse_args()
print(f'В скрипт передано: {args}')

# Примеры запуска в терминале
# python ExTerminalArgsKwargs.py 42 3.14 73 - В скрипт передано: Namespace(numbers=[42.0, 3.14, 73.0])

# python ExTerminalArgsKwargs.py --help # автоматически добавляется --help
# My first argument parser

# positional arguments:
#   N           press some numbers

# options:
#   -h, --help  show this help message and exit