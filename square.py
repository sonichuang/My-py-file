class Rec:
    def __init__(self, wid, hei):
        self.wid = wid
        self.hei = hei

    def __setattr__(self, name, value):
        if name == 'square':
            self.wid = value
            self.hei = value

        else:
            super().__setattr__(name, value) # 或者self.__dict__[name] = value

    def getarea(self):
        return self.wid * self.hei
    
