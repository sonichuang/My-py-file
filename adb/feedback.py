import os
import time 
os.system('adb shell input keyevent 26')
time.sleep(1)
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
time.sleep(10)
os.system('adb shell input keyevent 26')

