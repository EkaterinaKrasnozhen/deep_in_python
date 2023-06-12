import sys

data = [1, 'true', 3.123, 1, 'true', True, False]
for i in range(1, len(data)+1):
    print(i, data[i-1], id(data[i-1]), sys.getsizeof(data[i-1]), hash(data[i-1]), type(data[i-1]))
    
    #if str(data[i-1]).isdigit:
        #print("int")
    if type(data[i-1]) == bool:
        print("bool")
    elif isinstance(data[i-1], (int, float)):
        print("int")
    elif isinstance(data[i-1], str):
        print("string")
