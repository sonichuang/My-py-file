class A:
    num = 0
    def __init__(self):
        A.num += 1
        pass
    def __del__(self):
        A.num -= 1
        pass
