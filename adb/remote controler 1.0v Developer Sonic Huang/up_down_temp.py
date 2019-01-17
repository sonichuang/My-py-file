'''up_down_temp.py 本模块控制温度'''
import os
import time
def ut():
    os.system('adb shell am start -n com.weedle.haier_ac_remotes/com.weedle.haier_ac_remotes.InitialRoutingActivity')
    time.sleep(5)
    os.system('adb shell input tap 788 1837')

def dt():
    os.system('adb shell am start -n com.weedle.haier_ac_remotes/com.weedle.haier_ac_remotes.InitialRoutingActivity')
    time.sleep(5)
    os.system('adb shell input tap 778 2344')    
    
