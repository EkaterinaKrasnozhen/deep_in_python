from Animals import Animals


class Birds(Animals):
    def __init__(self, flying, *args, **kwargs):
        self.flying = flying
        super().__init__(*args, **kwargs)
        
    def get_unique_birds(self):
        if self.flying:
            return 'летающая'
        return 'не летающая'
    

if __name__ == '__main__':
    bird = Birds(True, 'Kate', 3)
    print(bird.get_unique_birds())