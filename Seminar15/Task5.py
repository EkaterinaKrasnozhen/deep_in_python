# Задание №5
# Дорабатываем задачу 4.
# Добавьте возможность запуска из командной строки.
# При этом значение любого параметра можно опустить. В
# этом случае берётся первый в месяце день недели, текущий
# день недели и/или текущий месяц.
import argparse
import datetime
from Task4 import input_text


def pars_date():
    parser = argparse.ArgumentParser(prog="Работа с датой")
    parser.add_argument('-d', metavar='d', default='1-й')
    parser.add_argument('-w', metavar='w', default=datetime.datetime.now().weekday())
    parser.add_argument('-m', metavar='m', default=datetime.datetime.now().month)
    args = parser.parse_args()
    return input_text(f'{args.d} {args.w} {args.m}')

# python Task5.py -d 1-ый -w четверг -m ноября
# 2023-11-02 00:00:00

if __name__ == "__main__":
    print(pars_date())
    

    