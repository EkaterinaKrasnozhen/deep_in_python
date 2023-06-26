import Task2_zagadki as zd

# txt = 'сто одежек и все без застежек'
# list_ans = 'капуста'
# ans, num = input(f'Отгадайте загадку {txt}. Введите от и количество попыток через пробел:').lower().split(' ')
# #print(ans, num)
# res = zd.get_info(txt, list_ans, ans, int(num))
# print(res)

res_dict = zd.ridd_dic()


for key, value in res_dict.items():
    ans, num = input(f'Отгадайте загадку {key}. Введите ответ и количество попыток через пробел:').lower().split(' ')
    result = zd.get_info(key, value, ans, int(num))
    print(result)
