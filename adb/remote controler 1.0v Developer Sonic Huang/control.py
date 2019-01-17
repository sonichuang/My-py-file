'''主程序'''
import os
import time
import sys
import easygui as eg
import ad_rid as ar
import capture_send as cs
import fan_power as fp
import on_off_pad as oop
import start_stop_air as ssa
import up_down_temp as udt
version = '远程遥控空调 1.0v    开发者:Sonic Huang'
oop.oop() #先点亮屏幕
def ask_feedback(): #定义一个反馈函数
    ask_f = eg.buttonbox('请选择', version, ('反馈', '返回主菜单', '直接退出'))
    if ask_f == '反馈':
        cs.cs()
        return 'continue'
    elif ask_f == '返回主菜单':
        return 'continue'
    else:
        return 'break'

while True: #询问是否确定APP的状态，再作出反应和操作
    ask_p = eg.buttonbox('是否确定APP状态？', version, ('确定', '反馈', '清除广告'))
    if ask_p == '确定':
        break
    if ask_p == '反馈':
        cs.cs()
        continue
    if ask_p == '清除广告':
        ask_a = eg.buttonbox('关闭键的位置', version, ('左上角', '中间', '左下角'))
        if ask_a == '左上角':
            ar.arl()
            continue
        elif ask_a == '中间':
            ar.arm()
            continue
        else:
            ar.arlb()
            continue
        
        
while True: #主要的控制
    ask_f = eg.buttonbox('请选择需要的功能', version, ('开关', '控温', '风力'))
    if ask_f == '开关':
        ssa.ssa()
        ask_fe = ask_feedback()
        if ask_fe == 'continue':
            continue
        else:
            break
        
    if ask_f == '控温':
        ask_ud = eg.buttonbox('请选择需要的功能', version, ('升温', '降温','维持'))
        if ask_ud == '升温':
            udt.ut()
        if ask_ud == '降温':
            udt.dt()
        ask_fe = ask_feedback()
        if ask_fe == 'continue':
            continue
        else:
            break
        
    if ask_f == '风力':
        fp.fp()
        ask_fe = ask_feedback()
        if ask_fe == 'continue':
            continue
        else:
            break
    else:
        break

oop.oop() #熄屏
sys.exit()
        
    
