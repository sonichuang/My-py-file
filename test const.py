#定义常量不成功 模块名 test const.py
class Const:
    def __getattr__(self, name):
        print('This attribut doesn\'t exsit.')
    def __getattribute__(self, name):
        return super().__getattribute__(name)
    def __setattr__(self, name, value):
        if isinstance(name, str) and name.isupper():
            super().__setattr__(name, value)
        else:
            print('The constant must be all upper letter.')
            raise TypeError
        
        
    
    


