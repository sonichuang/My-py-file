class Demo:
    def __getattr__(self, name):
        self.name = 'FishC'
        return self.name
