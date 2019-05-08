# coding=utf-8
import os
import time

from Android_TalkU.common.driver import get_driver

driver = get_driver()


def capture(name):
    # 截图
    img_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "..")) + '//screenshots//'
    time2 = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
    screen_save_path = img_folder + time2 + '_' + name + '.png'
    driver.get_screenshot_as_file(screen_save_path)


class ShowAds:

    @staticmethod
    def message_list():
        time.sleep(3)
        # 点击Contacts后再切换到Messages，用来获取广告
        driver.find_element_by_id("me.talkyou.app.im:id/ContactsLayout").click()
        time.sleep(3)
        # 点击More
        driver.find_element_by_id("me.talkyou.app.im:id/MoreLayout").click()
        time.sleep(3)
        # 点击Messages
        driver.find_element_by_id("me.talkyou.app.im:id/MessagesLayout").click()
        time.sleep(3)
        # 点击More
        driver.find_element_by_id("me.talkyou.app.im:id/MoreLayout").click()
        time.sleep(3)
        # 点击Messages
        driver.find_element_by_id("me.talkyou.app.im:id/MessagesLayout").click()
        time.sleep(3)
        # 获取截屏
        capture("Message_list")

    @staticmethod
    def team():
        time.sleep(3)
        # 点击小秘书TalkU Team
        driver.find_elements_by_id("me.talkyou.app.im:id/messages_first_listitem_layout")[2].click()
        time.sleep(3)
        # 获取截屏
        capture("Team")
        # 返回上一页
        driver.find_element_by_id("me.talkyou.app.im:id/chat_head_back").click()
        time.sleep(3)
        # 获取截屏
        capture("Message_list2")

    @staticmethod
    def us_sms():
        time.sleep(3)
        # 点击写短信
        driver.find_element_by_id("me.talkyou.app.im:id/messages_first_list_compose_imageview").click()
        time.sleep(3)
        # 点击第一个美国号码
        driver.find_elements_by_class_name("android.widget.LinearLayout")[1].click()
        time.sleep(3)
        # 获取截屏
        capture("SMS")
        # 返回上一页
        driver.find_element_by_id("me.talkyou.app.im:id/chat_head_back").click()

    @staticmethod
    def connect():
        time.sleep(3)
        # 点击Connect
        driver.find_element_by_id("me.talkyou.app.im:id/FindLayout").click()
        time.sleep(3)
        # 获取截屏
        capture("Connect")

    @staticmethod
    def lottery():
        time.sleep(3)
        # 点击Lottery
        driver.find_element_by_id("me.talkyou.app.im:id/more_private_phone_daily_lottery").click()
        time.sleep(3)
        # 获取截屏
        capture("Lottery")

    @staticmethod
    def redeem():
        time.sleep(3)
        # 点击More
        driver.find_element_by_id("me.talkyou.app.im:id/MoreLayout").click()
        time.sleep(3)
        # 点击Redeem
        driver.find_element_by_id("me.talkyou.app.im:id/more_redeem").click()
        time.sleep(3)
        # 获取截屏
        capture("Redeem")
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
        time.sleep(3)
        # 点击Check in Now
        driver.find_element_by_id("me.talkyou.app.im:id/checkin_button").click()
        time.sleep(2)
        # 获取截屏
        capture("GetCredits")
        time.sleep(8)
        # 获取截屏
        capture("GetCredits2")
        # 点击关闭小黑屏幕
        driver.find_element_by_id("me.talkyou.app.im: id / flurry_native_ad_close")
        # # 点击关闭全屏广告
        # driver.find_element_by_class_name("android.widget.ImageButton")
        time.sleep(3)
        # 获取截屏
        capture("GetCredits3")
        # 返回上一页
        driver.find_element_by_id("me.talkyou.app.im:id/checkin_back").click()


testShowAds = ShowAds()
testShowAds.message_list()
testShowAds.team()
testShowAds.us_sms()
testShowAds.connect()
testShowAds.redeem()
testShowAds.get_credits()


