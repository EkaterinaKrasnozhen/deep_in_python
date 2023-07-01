import json

# load файл и словарь

# with open ('user_json', 'a', encoding='utf-8') as f:
#     json_file = json.load(f)
    
# print(f'{type(json_file)=}=/n{json_file=}')
# print(f'{json_file['name']=}')
# print(f'{json_file['adress']['geo']=}') # двойная вложенность
# print(f'{json_file['email']=}') # если два мейла - список


# loads - строка
json_text = """
[
    {
        "user_id": 1,
        "id": 2,
        "title": "Hello my dear",
        "body": "yexy yexy"
    },
    {
        "user_id": 2,
        "id": 3,
        "title": "print some",
        "body": "no no no"
    }
]"""



# print(f'{type(json_text)}')
# json_list = json.loads(json_text)
# print(f'{type(json_list)} {len(json_list)=} {json_list=}')#<class 'list'> len(json_list)=2 json_list=[{'user_id': 1, 'id': 2, 'title': 'Hello my dear', 'body': 'yexy yexy'}, {'user_id': 2, 'id': 3, 'title': 'print some', 'body': 'no no no'}]

#dump - хотим сохранить инф в файл

my_dict = {
    "user_id": 1,
    "id": 2,
    "title": "Hello my dear",
    "body": ["yexy", "ryexy"],
    "children": [
        {
            "firstname": "Sviat",
            "age": 3,
        },
        {
            "firstname": "Yar",
            "age": 7,
        }
    ] 
}

# with open ('new_user_json', 'w') as f: # + ecoding utf-8 если русские симоволы
#     json.dump(my_dict, f) #ensure_ascii=False если знаем что все ок и хотим в файл кириллицу
    
# with open ('new_user_json', 'r', encoding='utf-8') as f:
#     new_dict = json.load(f)
    
# print(f'{type(my_dict)}{new_dict=}') #<class 'dict'>new_dict={'user_id': 1, 'id': 2, 'title': 'Hello my dear', 'body': ['yexy', 'ryexy'], 'children': [{'firstname': 'Sviat', 'age': 3}, {'firstname': 'Yar', 'age': 7}]}
# print(f'{new_dict["children"][0]=}') #new_dict["children"][0]={'firstname': 'Sviat', 'age': 3}

# #dumps - хотим в виде строки текста

# dict_to_json_text = json.dumps(my_dict) # (my_dict, ensure_ascii=False) если с русскими символами
# print(f'{type(dict_to_json_text)} {dict_to_json_text=}') # <class 'str'> dict_to_json_text='{"user_id": 1, "id": 2, "title": "Hello my dear", "body": ["yexy", "ryexy"], "children": [{"firstname": "Sviat", "age": 3}, {"firstname": "Yar", "age": 7}]}'

# indent() - сохраняем в неск строчек кода и цифрой передаем количство пробелов

# separators(',', ':') по умолчанию разделители

# sort_keys=True = по умолч False, если True - ключи  в алф порядке

# res = json.dumps(my_dict, indent=2, separators=(',', ':'), sort_keys=True)
# print(res)
# {
#   "body":[
#     "yexy",
#     "ryexy"
#   ],
#   "children":[
#     {
#       "age":3,
#       "firstname":"Sviat"
#     },
#     {
#       "age":7,
#       "firstname":"Yar"
#     }
#   ],
#   "id":2,
#   "title":"Hello my dear",
#   "user_id":1
# } 

a = 'Hello world'  
b = {key:value for key, value in enumerate(a)}
c = json.dumps(b, indent=2, separators=(';', '='))# заменив разделитель уже не json, рпеобразовать обратно не получится
print(c)
# {
#   "0"="H";
#   "1"="e";
#   "2"="l";
#   "3"="l";
#   "4"="o";
#   "5"=" ";
#   "6"="w";
#   "7"="o";
#   "8"="r";
#   "9"="l";
#   "10"="d"
# }