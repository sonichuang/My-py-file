class Ticket:
    default = 100
    def final(self, num, weekend = False, child = False):
        if weekend == True:
            self.rise = 1.2
        else:
            self.rise = 1
        if child == True:
            self.discount = 0.5
        else:
            self.discount = 1

        return self.default * self.rise * self.discount * num


    
adult = Ticket()
child = Ticket()
print(adult.final(2) + child.final(1, child = True))
