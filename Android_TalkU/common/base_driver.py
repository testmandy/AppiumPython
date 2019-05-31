# coding=utf-8
import time

from appium import webdriver
from Android_TalkU.utils.write_userconfig import WriteUserConfig

# '''
# 为了使类只能出现一个实例，我们可以使用 __new__ 来控制实例的创建过程
# 我们将类的实例和一个类变量 _instance 关联起来，如果 cls._instance 为 None 则创建实例，否则直接返回 cls._instance
# '''

class SuperDriver(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(SuperDriver, cls).__new__(cls, *args, **kwargs)
        return cls._instance


class BaseDriver(SuperDriver):
    def __init__(self):
        write_file = WriteUserConfig()
        self.device1 = write_file.get_value('deviceName')
        self.port = write_file.get_value('port')

    def android_driver(self):
        # server = Server()
        # port = server.port
        print("Android driver已连接的第一个设备：" + self.device1)
        capabilities = {
            "platformName": "Android",
            "deviceName": self.device1,
            # 可以通过newcommandtimeout将超时时间改长，超时时间可按照实际情况自定义
            "newCommandTimeout": "2000",
            "app": "C:\\Users\\user\\Downloads\\TU_Dev_4_8_0_unity_PN1-4.8.0.16498.apk",
            "appWaitActivity": "me.talkyou.app.im.activity.TalkuMainActivity",
            "appPackage": "me.talkyou.app.im",
            "noReset": "true"
        }
        driver = webdriver.Remote("http://127.0.0.1:" + str(self.port) + "/wd/hub", capabilities)
        time.sleep(5)
        return driver







