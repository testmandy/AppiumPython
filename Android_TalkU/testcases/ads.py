# coding=utf-8

import os
import HTMLTestRunner
import time
import unittest

from Android_TalkU.common.base_driver import BaseDriver
from Android_TalkU.utils.get_by_axis import GetByAxis
from Android_TalkU.utils.get_by_local import GetByLocal
from Android_TalkU.utils.server import Server


# 继承unittest.TestCase
class ShowAds(unittest.TestCase):
    # def tearDown(self):
    #     # 每个测试用例执行之后做操作
    #     print('111')
    #
    # def setUp(self):
    #     # 每个测试用例执行之前做操作
    #     print(22222)
    def setUp(self):
        # 实例化server
        self.server = Server()
        self.server.main()
        # 调用get_driver
        self.base_driver = BaseDriver()
        self.driver = self.base_driver.android_driver()
        print("开始运行APP")
        # 实例化GetByLocal
        self.starter = GetByLocal(self.driver)
        self.get_by_axis = GetByAxis()

    def capture(self, name):
        # 截图
        img_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "..")) + '//screenshots//'
        time2 = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        screen_save_path = img_folder + time2 + '_' + name + '.png'
        self.driver.get_screenshot_as_file(screen_save_path)

    def message_list(self):
        time.sleep(3)
        # 点击Contacts后再切换到Messages，用来获取广告
        self.starter.get_element("Contact_tab", "Contact").click()
        time.sleep(3)
        # 点击More
        self.starter.get_element("More_tab", "More").click()
        time.sleep(3)
        # 点击Messages
        self.starter.get_element("Messages_tab", "Messages").click()
        time.sleep(3)
        # 点击More
        self.starter.get_element("More_tab", "More").click()
        time.sleep(3)
        # 点击Messages
        self.starter.get_element("Messages_tab", "Messages").click()
        time.sleep(3)
        # 获取截屏
        self.capture("Message_list")

    def team(self):
        time.sleep(3)
        # 点击小秘书TalkU Team
        self.starter.get_element("TalkU_Team", "Messages")[0].click()
        time.sleep(3)
        # 获取截屏
        self.capture("Team")
        # 返回上一页
        self.starter.get_element("chat_back_button", "Messages").click()
        time.sleep(3)
        # 获取截屏
        self.capture("Message_list2")

    def us_sms(self):
        time.sleep(3)
        # 点击写短信
        self.starter.get_element("write_button", "Messages").click()
        time.sleep(3)
        # 点击第一个美国号码
        self.starter.get_element("number_list", "Messages")[1].click()
        time.sleep(3)
        # 获取截屏
        self.capture("SMS")
        # 返回上一页
        self.starter.get_element("chat_back_button", "Messages").click()

    def connect(self):
        time.sleep(3)
        # 点击Connect
        self.starter.get_element("Connect_tab", "Connect").click()
        time.sleep(3)
        # 获取截屏
        self.capture("Connect")

    def lottery(self):
        time.sleep(3)
        # 点击Lottery
        self.starter.get_element("lottery", "Connect").click()
        time.sleep(3)
        # 获取截屏
        self.capture("Lottery")

    def redeem(self):
        time.sleep(3)
        # 点击More
        self.starter.get_element("More_tab", "More").click()
        time.sleep(3)
        # 点击Redeem
        self.starter.get_element("Redeem", "More").click()
        time.sleep(3)
        # 获取截屏
        self.capture("Redeem")
        # 返回上一页
        self.starter.get_element("redeem_back_button", "More").click()

    def get_credits(self):
        time.sleep(3)
        # 点击Get Free Credits
        self.starter.get_element("GetMoreCredits", "More").click()
        time.sleep(3)
        # 点击Check-in
        self.starter.get_element("Checkin", "More").click()
        time.sleep(3)
        # 点击Check in Now
        self.starter.get_element("CheckinNow", "More").click()
        time.sleep(2)
        # 获取截屏
        self.capture("GetCredits")
        time.sleep(8)
        # 获取截屏
        self.capture("GetCredits2")
        # 点击关闭小黑屏幕
        self.starter.get_element("FN_ad_close", "More")
        # # 点击关闭全屏广告
        # driver.find_element_by_class_name("android.widget.ImageButton")
        time.sleep(3)
        # 获取截屏
        self.capture("GetCredits3")
        # 返回上一页
        self.starter.get_element("checkin_back_button", "More").click()


if __name__ == '__main__':
    test_suite = unittest.TestSuite()  # 创建一个测试集合
    test_suite.addTest(ShowAds('message_list'))  # 测试套件中添加测试用例
    # test_suite.addTest(unittest.makeSuite(ShowAds))#使用makeSuite方法添加所有的测试方法
    # 打开一个保存结果的html文件
    now = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())
    filename = "E:\\PycharmProjects\\TalkUAds_UITest_Python\\Android_TalkU\\report\\" + now + "_result.html"
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='api测试报告', description='测试情况')
    # 生成执行用例的对象
    runner.run(test_suite)
    # 执行测试套件


