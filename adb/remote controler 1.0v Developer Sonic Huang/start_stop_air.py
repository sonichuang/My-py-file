'''start_stop_air.py 本模块控制开关空调'''
import os
import time
def ssa():
    os.system('adb shell am start -n com.weedle.haier_ac_remotes/com.weedle.haier_ac_remotes.InitialRoutingActivity')
    time.sleep(5)
    os.system('adb shell input tap 1069 1297')


