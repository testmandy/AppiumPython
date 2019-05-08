# coding=utf-8
import os
import time

from Android_TalkU.common import driver


class Capture:
    @staticmethod
    def capture():
        # 截图
        img_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "..")) + '//screenshots//'
        time2 = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        screen_save_path = img_folder + time2 + '.png'
        driver.get_screenshot_as_file(screen_save_path)



