class Mydes:
    def __init__(self, va = None, na = None):
        self.val = va
        self.nam = na
            
    def __get__(self, instance, owner):
        print('Getting the variable: %s'  % self.nam)
        return  self.val

    def __set__(self, instance, value):
        print('Setting the variable: %s'  % self.nam)
        self.val = value

    def __delete__(self, instance):
        print('Deleting the variable: %s'  % self.nam)
        print('You can\'t delete this variable.')

class Test:
    x = Mydes(10, 'x')


