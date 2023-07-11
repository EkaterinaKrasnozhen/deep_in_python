from Animals import Animals


class Birds(Animals):
    def __init__(self, flying, *args, **kwargs):
        self.flying = flying
        super().__init__(*args, **kwargs)