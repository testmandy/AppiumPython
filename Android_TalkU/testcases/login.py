# coding=utf-8
import time
from Android_TalkU.common.driver import get_driver

driver = get_driver()


class Login:

    def __init__(self, telephone, password):
        self.telephone = telephone
        self.password = password

    @staticmethod
    def go_login():
        time.sleep(3)
        # 点击-Already have account?
        driver.find_element_by_id("me.talkyou.app.im:id/tv_already_have_account").click()

    def login(self):
        time.sleep(2)
        # 输入手机号
        driver.find_element_by_id("me.talkyou.app.im:id/signup_login_phone_number_area").send_keys(self.telephone)
        # 点击Continue进入下一步
        driver.find_element_by_class_name("android.widget.Button").click()
        time.sleep(2)
        # 输入密码
        driver.find_element_by_id("me.talkyou.app.im:id/password_login_edit").send_keys(self.password)
        # 点击Login登录
        driver.find_element_by_id("me.talkyou.app.im:id/password_login_btn").click()
        time.sleep(2)
        # 出现弹窗，点击确认
        driver.find_element_by_id("me.talkyou.app.im:id/button1").click()
        time.sleep(2)

    @staticmethod
    def logout():
        # 点击More
        driver.find_element_by_id("me.talkyou.app.im:id/MoreLayout").click()
        time.sleep(2)
        # 点击Settings
        driver.find_element_by_id("me.talkyou.app.im:id/more_settings").click()
        time.sleep(2)
        # 点击Account Settings
        driver.find_element_by_id("me.talkyou.app.im:id/myaccount_settings").click()
        time.sleep(2)
        # 点击My Devices on TalkU
        driver.find_element_by_id("me.talkyou.app.im:id/more_my_device").click()
        time.sleep(2)
        # 点击注销按钮
        driver.find_element_by_id("me.talkyou.app.im:id/more_my_deactivate").click()
        time.sleep(6)
        # 出现弹窗，点击确认注销
        driver.find_element_by_id("me.talkyou.app.im:id/button1").click()
        time.sleep(2)
        # 出现弹窗，再次点击确认
        driver.find_element_by_id("me.talkyou.app.im:id/button3").click()


testLogin = Login("3159782580", "123456")
testLogin.go_login()
testLogin.login()
testLogin.logout()


