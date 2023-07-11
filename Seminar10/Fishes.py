from Animals import Animals


class Fishes(Animals):
    def __init__(self, area, *args, **kwargs):
        self.area = area
        super().__init__(*args, **kwargs)
        
    def get_unique_info(self):
        