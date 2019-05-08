# coding=utf-8
from appium import webdriver


def get_driver():
    capabilities = {
        "platformName": "Android",
        "deviceName": "159beaa8",
        "app": "C:\\Users\\user\\Downloads\\TalkU.apk",
        "appPackage": "me.talkyou.app.im",
        "noReset": "true"
    }
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", capabilities)
    return driver

