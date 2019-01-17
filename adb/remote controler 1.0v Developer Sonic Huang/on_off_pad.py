'''on_off_pad.py 点亮或者关闭屏幕'''
import os
import time
def oop():
    os.system('adb shell input keyevent 26')


