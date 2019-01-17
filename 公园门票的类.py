class Ticket:
    def __init__(self, weekend = False, child = False):
        self.default = 100
        if weekend:
            self.rise = 1.2
        else:
            self.rise = 1
        if child:
            self.discount = 0.5
        else:
            self.discount = 1
    def final(self, num):
        return self.default * self.rise * self.discount * num


adult = Ticket()
child = Ticket(child = True)
print(adult.final(2) + child.final(1))

