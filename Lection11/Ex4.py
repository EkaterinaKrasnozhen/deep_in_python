class Count:
    _count = 0
    _last = None
    
    def __new__(cls, *args, **kwargs): # дает создать три экзмпляра и потом будет возращать всегда последний третий
        if cls._count < 3:
            cls._last = super().__new__(cls)
        cls._count += 1
        return cls._last
    
    def __init__(self, name: str):
        self.name = name