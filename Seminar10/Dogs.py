from Animals import Animals


class Dogs(Animals):
    def __init__(self, wool, *args, **kwargs):
        self.wool = wool
        super().__init__(*args, **kwargs)