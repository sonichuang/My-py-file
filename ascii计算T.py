class AsciiC:
    def __init__(self, k = ''):
        self.asciin = 0
        if isinstance(k, str):
            for i in k:
                self.asciin += ord(i)
        else:
            print('The argument is wrong.')
    def __add__(self, other):
        return self.asciin + other.asciin
    def __sub__(self, other):
        return self.asciin - other.asciin
    def __mul__(self, other):
        return self.asciin * other.asciin
    def __truediv__(self, other):
        return self.asciin / other.asciin
    def __floordiv__(self, other):
        return self.asciin // other.asciin



