class Hero:
    def __init__(self, name, gender, age, power):
        self.name = name
        self.gender = gender
        self.age = age
        self.power = power
    def ingrass(self):
        self.power = self.power - 200
    def practice(self):
        self.power = self.power + 100
    def group(self):
        self.power = self.power - 500
    def result(self):
        print('name:%s gender:%s age:%s power:%s' % (self.name, self.gender, self.age, self.power))

cjk = Hero('cjk', 'female', 18, 1000)
cjk.ingrass()
cjk.result()
jack = Hero('jack', 'male', 22, 1500)
jack.practice()
jack.result()
jame = Hero('jame', 'male', 28, 1300)
jame.group()
jame.result()
    

