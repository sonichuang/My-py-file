def asciin(k):
    n = 0
    for i in list(k):
            n += ord(i)
    return n



class AsciiC(str):
    def __add__(self, other):
        return asciin(self) + asciin(other)
    def __sub__(self, other):
        return asciin(self) - asciin(other)
    def __mul__(self, other):
        return (asciin(self)) * (asciin(other))
    def __truediv__(self, other):
        return asciin(self) / asciin(other)
    def __floordiv__(self, other):
        return asciin(self) // asciin(other)



