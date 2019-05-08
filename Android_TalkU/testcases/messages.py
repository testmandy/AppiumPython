# coding=utf-8

import time

from Android_TalkU.common.driver import get_driver
from Android_TalkU.utils.capture import capture

driver = get_driver()


class ShowAds:

    # def __init__(self):

    @staticmethod
    def message_list():
        time.sleep(3)
        # 点击Contacts后再切换到Messages，用来获取广告
        driver.find_element_by_id("me.talkyou.app.im:id/ContactsLayout").click()
        driver.find_element_by_id("me.talkyou.app.im:id/MessagesLayout").click()
        time.sleep(3)
        # 获取截屏
        capture()

    @staticmethod
    def team():
        time.sleep(3)
        # 点击小秘书TalkU Team
        driver.find_element_by_id("me.talkyou.app.im:id/messages_first_listitem_layout").click()
        time.sleep(3)
        # 获取截屏
        capture()
        # 返回上一页
        driver.find_element_by_id("me.talkyou.app.im:id/chat_head_back").click()

    @staticmethod
    def us_sms():
        time.sleep(3)
        # 点击写短信
        driver.find_element_by_id("me.talkyou.app.im:id/messages_first_list_compose_imageview").click()
        time.sleep(3)
        # 点击第一个美国号码
        driver.find_elements_by_class_name("android.widget.LinearLayout")[1].click()
        # 获取截屏
        capture()
        # 返回上一页
        driver.find_element_by_id("me.talkyou.app.im:id/chat_head_back").click()

    @staticmethod
    def connect():
        time.sleep(3)
        # 点击Connect
        driver.find_element_by_id("me.talkyou.app.im:id/FindLayout").click()
        time.sleep(3)
        # 获取截屏
        capture()

    @staticmethod
    def redeem():
        time.sleep(3)
        # 点击More
        driver.find_element_by_id("me.talkyou.app.im:id/MoreLayout").click()
        time.sleep(3)
        # 点击Redeem
        driver.find_element_by_id("me.talkyou.app.im:id/more_redeem").click()
        # 获取截屏
        capture()
        # 返回上一页
        driver.find_element_by_id("me.talkyou.app.im:id/view_back").click()

    @staticmethod
    def get_credits():
        time.sleep(3)
        # 点击Get Free Credits
        driver.find_element_by_id("me.talkyou.app.im:id/more_get_credits").click()
        time.sleep(3)
        # 点击Check-in
        driver.find_element_by_id("me.talkyou.app.im:id/activity_earn_free_credits_daily_checkin").click()
        driver.find_element_by_id("me.talkyou.app.im:id/checkin_button").click()
        # 获取截屏
        capture()
        # 返回上一页
        driver.find_element_by_id("me.talkyou.app.im:id/checkin_back").click()


testShowAds = ShowAds()
testShowAds.message_list()
testShowAds.team()
testShowAds.us_sms()
testShowAds.connect()
testShowAds.redeem()
testShowAds.get_credits()


