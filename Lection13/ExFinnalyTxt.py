file = open('text.txt', 'r', encoding='utf-8')
try:
    data = file.read().split()
    print(data[len(data)])
finally:
    print('Закрываю файл')
    file.close()# хоть и будт ошибка файл будет закрыт, выполяняется в любом случае, но лучше использовать with open который всегла закрывает и так