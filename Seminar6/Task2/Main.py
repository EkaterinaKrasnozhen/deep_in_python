import Task2_zagadki as zd

txt = 'сто одежек и все без застежек'
list_ans = 'капуста'
ans, num = input(f'Отгадайте загадку {txt}. Введите от и количество попыток через пробел:').lower().split(' ')
#print(ans, num)
res = zd.get_info(txt, list_ans, ans, int(num))
print(res)