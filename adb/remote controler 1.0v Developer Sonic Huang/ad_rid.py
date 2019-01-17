'''ad_rid.py 这个模块的作用是清除广告'''
import os
import time
def arl():#调出遥控板程序并点击页面左上角的关闭按钮，关闭广告
    os.system('adb shell am start -n com.weedle.haier_ac_remotes/com.weedle.haier_ac_remotes.InitialRoutingActivity')
    time.sleep(3)
    os.system('adb shell input tap 53 71')

def arm():#调出遥控板程序并点击页面中间的关闭按钮，关闭广告
    os.system('adb shell am start -n com.weedle.haier_ac_remotes/com.weedle.haier_ac_remotes.InitialRoutingActivity')
    time.sleep(3)
    os.system('adb shell input tap 445 1382')

def arlb():
    os.system('adb shell am start -n com.weedle.haier_ac_remotes/com.weedle.haier_ac_remotes.InitialRoutingActivity')
    time.sleep(3)
    os.system('adb shell input tap 409 2448')

    

