# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 00:23:10 2017

@author: WangTong
"""

import pyautogui as pag
import time

pag.FAILSAFE = True
output=open('C:\\Users\\WangTong\\Desktop\\寻找gmail\\output.txt','w+')
pag.moveTo(100,800)
pag.scroll(100)
pag.moveTo(500,1720)#右移
pag.dragTo(1000,1720,0.5)
try:
    for num in range(800000,1000000):
        flag=True
        pag.moveTo(1057,754)#移动到选择用户名窗口
        pag.click()
        pag.hotkey('ctrl','a')
        pag.press('delete')
        pag.typewrite(str(num))
        pag.moveTo(800,754)#移动到选择用户名窗口
        pag.click()
        time.sleep(1)
        img = pag.screenshot(region=(540, 440, 10,1))
        for i in range(1,10):
            (r,g,b)=img.getpixel((i,0))
            if g<100:
                flag=False# 出现了红框，说明该用户名已经有人用了
                break
        if flag:
            #之前可能是网速较慢，延时5s再判断一次
            flag=True
            pag.click()
            time.sleep(5)
            img = pag.screenshot(region=(540, 440, 10,1))
            for i in range(1,10):
                (r,g,b)=img.getpixel((i,0))
                if g<100:
                    flag=False
                    break
            if flag:
                #这个密码可以使用，但也存在google挂掉的情况，无论如何，先注册试试
                pag.moveTo(1057,870)#设置密码
                pag.click()
                pag.hotkey('ctrl','a')
                pag.press('delete')
                pag.typewrite('dasdhasiduha')
                pag.moveTo(1057,990)#确认密码
                pag.click()
                pag.hotkey('ctrl','a')
                pag.press('delete')
                pag.typewrite('dasdhasiduha')
                pag.moveTo(1450,1680)#下一步
                pag.click()
                pag.moveTo(920,1520)#按键
                pag.click()
                pag.moveTo(1250,1580)#我同意
                pag.click()
                time.sleep(4)
                img = pag.screenshot(region=(160, 450, 1 ,1))
                (r,g,b)=img.getpixel((0, 0))
                #可以(74, 140, 246)
                #不可以(255, 255, 255)
                if r<150:#注册失败
                    print(num,'可以')
                    pag.moveTo(40,100)#返回上一层
                    pag.click()
                    time.sleep(1)
                    pag.scroll(100)
                    pag.moveTo(500,1720)#右移
                    pag.dragTo(1000,1720,0.5)
                    output.write(str(num)+':Ok')
                    output.write('\n')
                else:#注册成功
                    print(num,'不可以')
                    pag.scroll(100)
                    pag.moveTo(500,1720)#右移
                    pag.dragTo(1000,1720,0.5)
                    output.write(str(num)+':No')
except:
    print('error')
finally:
    output.close()
