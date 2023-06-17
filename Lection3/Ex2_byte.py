text = "hellp world"
res = text.encode('utf-8')
print(res, type(res)) #b'hellp world' <class 'bytes'>
text2 = "Привет мир"
res2 = text2.encode('utf-8')
print(res2)#b'\xd0\x9f\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82 \xd0\xbc\xd0\xb8\xd1\x80'

x = bytes(b'\xd0\x9f\x88') #неизменяемая последовательность
y = bytearray(b'\xd0\x9f\x88')#изменяемый массив
print(f'{x=}\n{y=}')#x=b'\xd0\x9f\x88'
#                    y=bytearray(b'\xd0\x9f\x88')