# coding=utf-8
import os
import time

from Android_TalkU.testcases.messages import driver


def take_screenShot(self, name="takeShot"):
    '''
    method explain:获取当前屏幕的截图
    parameter explain：【name】 截图的名称
    Usage:
        device.take_screenShot(u"个人主页")   #实际截图保存的结果为：2018-01-13_17_10_58_个人主页.png
    '''
    day = time.strftime("%Y-%m-%d", time.localtime(time.time()))
    fq = "..\\screenShots\\" + day
    # fq =os.getcwd()[:-4] +'screenShots\\'+day    根据获取的路径，然后截取路径保存到自己想存放的目录下
    tm = time.strftime("%Y-%m-%d_%H_%M_%S", time.localtime(time.time()))
    type = '.png'
    filename = ""
    if os.path.exists(fq):
        filename = fq + "\\" + tm + "_" + name + type
    else:
        os.makedirs(fq)
        filename = fq + "\\" + tm + "_" + name + type
    # c = os.getcwd()
    # r"\\".join(c.split("\\"))     #此2行注销实现的功能为将路径中的\替换为\\
    self.driver.get_screenshot_as_file(filename)


def capture():
    # 截图
    img_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "..")) + '//screenshots//'
    time2 = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
    screen_save_path = img_folder + time2 + '.png'
    driver.get_screenshot_as_file(screen_save_path)
