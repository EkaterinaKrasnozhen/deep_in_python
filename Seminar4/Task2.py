# Напишите функцию, которая принимает строку текста.
# Сформируйте список с уникальными кодами Unicode каждого
# символа введённой строки отсортированный по убыванию.

txt = str(input('Введите строку: '))#hello

def print_ord(text):
    dict1 = {}
    for char in text:
        dict1.setdefault(char, ord(char))
    print(sorted(dict1.items(), key=lambda item: item[1]))#[('e', 101), ('h', 104), ('l', 108), ('o', 111)]
    
print_ord(txt)