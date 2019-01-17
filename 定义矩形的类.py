class Rectangle:
    long = 5.00
    width = 4.00
    def getRect(self):
        print('这个矩形的长是：%3.2f, 宽是：%3.2f。' % (self.long, self.width))
    def setRect(self):
        print('请输入矩形的长和宽...')
        self.long = int(input('长：'))
        self.width = int(input('宽：'))
    def getArea(self):
        print(self.long * self.width)
