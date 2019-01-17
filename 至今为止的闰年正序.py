'''按照正序打印至今的闰年'''
class Leapyears:
    def __init__(self, m = 2018):
        self.x = 0
    def __iter__(self):
        return self
    def __next__(self):
        self.x += 4
        if self.x >= 2018:
            raise StopIteration
        return self.x

leapyears = Leapyears()
for x in leapyears:
    if x >= 2000:
        print(x)
