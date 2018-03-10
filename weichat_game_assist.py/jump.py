##########################
#
# 微信小程序跳一跳辅助工具
# 2018.1.7 @czh
#  
##########################

# 准备工具：adb驱动，安卓手机及其调试模式
# 游戏原理是根据按住屏幕的时间来跳出相应的距离

########################################################################
# 实现原理：获取手机的实时截图 ——> 鼠标点击起始位置和落地位置 ——> 计算两个点的距离 
#         ——> 计算按压时间 ——> 发送按压指令 ——> 重新刷新手机截图
########################################################################

import os
import PIL, numpy
import matplotlib.pyplot as plt 
import matplotlib.animation import FuncAnimation
import time

need_update = True

def get_screen_image():
    # python启动系统命令保存手机截图到手机根目录下，下载手机里的截图保存在PC当前文件中，打开图片并将其转化为多维数组
    os.system('.\\adb shell screencap -p /sdcard/screen.png')  
    os.system('.\\adb pull /sdcard/screen.png')
    return numpy.array(PIL.Image.open('screen.png'))

def on_click(event, coor=[]):
    global need_update
    coor.append((event.xdata, event.ydata))
    if len(coor) == 2:
        jump_to_next(coor.pop(), coor.pop())
        need_update = True
        
def jump_to_next(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    distance = ((x1-x2)**2 + (y1-y2)**2)**0.5  # 计算两个点的距离
    os.system('adb shell input swipe 320 410 320 410 {}'.format(int(distance*1.35)))  # 此游戏一个像素点距离需要按压1.35ms
    

def update_screen_image(frame):
    # 更新图片，重画图片
    global need_update
    if need_update:
        time.sleep(1)
        axes_image.set_array(get_screen_image())
        need_update = False
    return axes_image,


figure = plt.figure()  # 创建一个空白的图片对象
axes_image = plt.imshow(get_screen_image(), animated = True)  # 将获取的图片画在坐标轴上
# 绑定事件，鼠标点击一个位置并触发一个回调函数
figure.canvas.mpl_connect('button_press_event', on_click)
ani = FuncAnimation(figure, update_screen_image, interval = 50, blit = True) # 刷新的函数，会一直循环
plt.show()
    



