class StrPro(str):
    
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls, *args, **kwargs)
        return instance
    
    def __rmul__(self, other: str): # правое умножение
        words = other.split()
        result = self.join(words)
        return StrPro(result)
        
text = 'Каждый охотник желает знать где сидит фазан'
s = StrPro(' (=^.^=) ')
print(f'{text = }\n{s = }')#text = 'Каждый охотник желает знать где сидит фазан' s = ' (=^.^=) '
print(text * s)#Каждый (=^.^=) охотник (=^.^=) желает (=^.^=) знать (=^.^=) где (=^.^=) сидит (=^.^=) фазан
#print(s * text) # TypeError: 'str' object cannot be interpreted as an integer
