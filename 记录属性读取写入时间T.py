import time

class R:
    def __init__(self, initval=None, name=None):
        self.val = initval
        self.name = name
        self.filename = "C:\\Users\\vulcanten\\desktop\\record.txt"

    def __get__(self, instance, owner):
        with open(self.filename, 'a', encoding='utf-8') as f:
            f.write("%s 变量于北京时间 %s 被读取，%s = %s\n" % \
                    (self.name, time.ctime(), self.name, str(self.val)))
        return self.val

    def __set__(self, instance, value):
        with open(self.filename, 'a', encoding='utf-8') as f:
            f.write("%s 变量于北京时间 %s 被修改, %s = %s\n" % \
                    (self.name, time.ctime(), self.name, str(value)))
        self.val = value
