'''capture_send.py 本模块的作用是截取遥控器APP的页面, 来向用户微信反馈所处的状态。'''
import os
import time
def cs():#截屏并发微信
    os.system('adb shell am start -n com.weedle.haier_ac_remotes/com.weedle.haier_ac_remotes.InitialRoutingActivity')
    time.sleep(5)    
    os.system('adb shell /system/bin/screencap -p /sdcard/screen.png')
    time.sleep(1)
    os.system('adb shell am start -n com.tencent.mm/.ui.LauncherUI')
    time.sleep(5)
    os.system('adb shell input tap 753 214')
    time.sleep(1)
    os.system('adb shell input tap 1545 2526')
    time.sleep(1)
    os.system('adb shell input tap 232 2208')
    time.sleep(1)
    os.system('adb shell input tap 246 333')
    time.sleep(1)
    os.system('adb shell input tap 789 2526')
    time.sleep(1)
    os.system('adb shell input tap 1497 95')


