import pyautogui as pag
# 图像操作
# 获取屏幕分辨率
screenWidth, screenHeight = pag.size()
print('屏幕宽:'+str(screenWidth)+"----屏幕高:"+str(screenHeight))

# 截屏功能
#  返回一个Pillow/PIL的Image对象
img = pag.screenshot()
img.save('foo.png')
pag.screenshot('foo.png')

# 获得某个坐标的像素
(r,g,b)=img.getpixel((50, 200))
print('r:'+str(r)+"----g:"+str(g)+"----b:"+str(b))

# 判断屏幕坐标的像素是不是等于某个值
ifEqual=pag.pixelMatchesColor(50, 200, (30, 132, 153))
#True

# 如果你不需要截取整个屏幕，还有一个可选的region参数。你可以把截取区域的左上角XY坐标值和宽度、高度传入截取
img = pag.screenshot(region=(0, 0, 300 ,400))

# 在屏幕上找到按钮所在的坐标。其实很简单，首先对你要点击的按钮截个图，就叫button.png吧。然后使用locateOnScreen函数找到按钮所在的位置
pag.locateOnScreen('foo.png')
# (643, 745, 70, 29)

# locateOnScreen其实就是简单的颜色对比，如果有一个像素不匹配，它就会返回None。这个函数返回了匹配图形的坐标，找到中间点：
x, y = pag.center((643, 745, 70, 29))  # 获得中心点
pag.click(x, y)

# locateAllOnScreen()：找到所有匹配的位置坐标。

# 要检查XY坐标是否在屏幕上，需要用onScreen()函数来检验，如果在屏幕上返回True：
pag.onScreen(0, 0) #True
pag.onScreen(0, -1) #False

# 鼠标操作
# 获取当前鼠标的坐标
currentMouseX, currentMouseY = pag.position()

# 鼠标点击
pag.click()

# 使用click()函数发送虚拟鼠标点击，默认情况下在鼠标所在的位置点击左键。函数原型：
# pag.click(x=cur_x, y=cur_y, button='left')
# x，y是要点击的位置，默认是鼠标当前位置
# button是要点击的按键，有三个可选值：‘left’, ‘middle’, ‘right’

# 每个按键按下和松开两个事件可以分开处理：
# pag.mouseDown(x=moveToX, y=moveToY, button='left')
# pag.mouseUp(x=moveToX, y=moveToY, button='left')

# 双击
pag.doubleClick()

# 右击
pag.rightClick()

# 中击
pag.middleClick()

# 鼠标移动 缓动/渐变函数让鼠标2秒后移动到(x,y)位置
pag.moveTo(x,y,duration=2, tween=pag.easeInOutQuad) #  绝对坐标
# 鼠标移动 缓动/渐变函数让鼠标2秒后相对当前鼠标位置移动到(x,y)的地方
pag.moveRel(x,y,duration=2, tween=pag.easeInOutQuad) # 相对坐标


# 鼠标拖拽
# 注意：duration时间不能太短，拖动太快有些系统会吃不消
# pag.dragTo(x,y,duration,)
# pag.dragRel(x,y,duration)

# 多次点击
# 可以设置clicks参数，还有interval参数可以设置每次单击之间的时间间隔。例如：
#  双击左键
pag.click(clicks=2)
#  两次单击之间停留0.25秒
pag.click(clicks=2, interval=0.25)
#  三击右键
pag.click(button='right', clicks=2, interval=0.25)

# 滚轮
# 使用函数scroll()，它只接受一个整数。如果值为正往上滚，值为负往下滚。

pag.scroll(200)

# 缓动/渐变（Tween / Easing）函数
# 缓动/渐变函数的作用是让光标的移动更炫。如果你不需要用到的话，你可以忽略这些
# 缓动/渐变函数可以改变光标移动过程的速度和方向。通常鼠标是匀速直线运动，这就是线性缓动/渐变函数。PyAutoGUI有30种缓动/渐变函数，可以通过pyautogui.ease*?查看。其中，pyautogui.easeInQuad()函数可以用于moveTo()，moveRel()，dragTo()和dragRel()函数，光标移动呈现先慢后快的效果，整个过程的时间还是和原来一样。而pyautogui.easeOutQuad函数的效果相反：光标开始移动很快，然后慢慢减速。pyautogui.easeOutElastic是弹簧效果，首先越过终点，然后再反弹回来。例如：

#  开始很慢，不断加速
pag.moveTo(100, 100, 2, pag.easeInQuad)
#  开始很快，不断减速
pag.moveTo(100, 100, 2, pag.easeOutQuad)
#  开始和结束都快，中间比较慢
pag.moveTo(100, 100, 2, pag.easeInOutQuad)
#  一步一徘徊前进
pag.moveTo(100, 100, 2, pag.easeInBounce)
#  徘徊幅度更大，甚至超过起点和终点
pag.moveTo(100, 100, 2, pag.easeInElastic)

# 键盘操作
# 输入字符串

pag.typewrite('Hello world')

# 上面的字符串是一次输入，为了唬人可以延迟输入

pag.typewrite('Hello world!', 0.25)

# PyAutoGUI键盘表：
# 字符串	代表按键
# ‘enter’(或‘return’ 或 ‘\n’)	回车
# ‘esc’	ESC键
# ‘shiftleft’, ‘shiftright’	左右SHIFT键
# ‘altleft’, ‘altright’	左右ALT键
# ‘ctrlleft’, ‘ctrlright’	左右CTRL键
# ‘tab’ (‘\t’)	TAB键
# ‘backspace’, ‘delete’	BACKSPACE 、DELETE键
# ‘pageup’, ‘pagedown’	PAGE UP 和 PAGE DOWN键
# ‘home’, ‘end’	HOME 和 END键
# ‘up’, ‘down’, ‘left’,‘right’	箭头键
# ‘f1’, ‘f2’, ‘f3’….	F1…….F12键
# ‘volumemute’, ‘volumedown’,‘volumeup’	有些键盘没有
# ‘pause’	PAUSE键
# ‘capslock’, ‘numlock’,‘scrolllock’	CAPS LOCK, NUM LOCK, 和 SCROLLLOCK 键
# ‘insert’	INS或INSERT键
# ‘printscreen’	PRTSC 或 PRINT SCREEN键
# ‘winleft’, ‘winright’	Win键
# ‘command’	Mac OS X command键
# keyDown()：按下某个键
# keyUp()：松开某个键
# press()：一次完整的击键，前面两个函数的组合。
# hotkey(‘ctrl’,’c’)：热键函数
# 消息弹窗函数

pag.alert('这个消息弹窗是文字+OK按钮')
pag.confirm('这个消息弹窗是文字+OK+Cancel按钮')
pag.prompt('这个消息弹窗是让用户输入字符串，单击OK')
#返回用户输入的字符串，如果用户什么都不输入，则返回None

# 保护措施（Fail-Safes）
# Python移动鼠标、点击键盘非常快，有可以导致其他应用出现问题。在这种情况下，程序可能会失控（即使是按照你的意思执行的），那时就需要中断。如果鼠标还在自动操作，就很难在程序窗口关闭它。

# 为了能够及时中断，PyAutoGUI提供了一个保护措施。当pyautogui.FAILSAFE = True时，如果把鼠标光标在屏幕左上角，PyAutoGUI函数就会产生pyautogui.FailSafeException异常。如果失控了，需要中断PyAutoGUI函数，就把鼠标光标在屏幕左上角。要禁用这个特性，就把FAILSAFE设置成False
pag.FAILSAFE = False;

# 通过把pyautogui.PAUSE设置成float或int时间（秒），可以为所有的PyAutoGUI函数增加延迟。默认延迟时间是0.1秒。在函数循环执行的时候，这样做可以让PyAutoGUI运行的慢一点，非常有用。例如：

pag.PAUSE = 2.5
pag.moveTo(100,100);
pag.click()


