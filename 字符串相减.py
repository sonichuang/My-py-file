class Substr(str):
    def __sub__(self, other):
        c = ''
        for b in [a for a in self if a != other]:
            c += b
        return c
            


a = Substr('i love you!!!!!!!!')
b = Substr('!')
print(a - b)
