'''fan_power.py 模块控制风力'''
import os
import time
def fp():
    os.system('adb shell am start -n com.weedle.haier_ac_remotes/com.weedle.haier_ac_remotes.InitialRoutingActivity')
    time.sleep(5)
    os.system('adb shell input tap 783 2092')
