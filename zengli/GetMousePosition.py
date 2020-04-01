import os
import time
import pyautogui as pag
try:
    while True:
        x,y = pag.position() #返回鼠标的坐标
        posStr = "鼠标当前位置:  "+str(x).rjust(4)+','+str(y).rjust(4)+"   (Press Ctrl-C to end)"
        print (posStr)#打印坐标
        time.sleep(1.5)
        os.system('cls')#清空屏幕
except  KeyboardInterrupt:
    print ('end....')