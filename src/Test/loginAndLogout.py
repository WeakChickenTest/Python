from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import os
from time import sleep

# 定义设备信息
dev = {
    "appium:drvice": "android",
    "platformName": "Android",
    "platformVersion": "11",
    "deviceName": "OPPO A53",
    "udid": "IJSC6TRGXSIRTOXK",
    "appActivity": ".activity.ActivityWelcome mCallingUid=2000",
    "appPackage": "com.netease.edu.study",
    "noReset": "true"
}
dr = webdriver.Remote(command_executor='http://127.0.0.1:4723/wd/hub', desired_capabilities=dev)


def login(mobile, password):
    # 等待某个元素出现，元素出现后立即执行后边的代码
    # WebDriverWait(dr, int 等待时长).until(lambda x: x.find_element(str 元素类型, str 元素的值))
    WebDriverWait(dr, 10).until(lambda x: x.find_element("id", "com.netease.edu.study:id/tab_account"))
    dr.find_element("id", "com.netease.edu.study:id/tab_account").click()  # 点击【我的】tab
    WebDriverWait(dr, 1).until(lambda x: x.find_element("id", "com.netease.edu.study:id/account_default_text"))
    dr.find_element("id", "com.netease.edu.study:id/account_default_text").click()  # 点击【登录/注册】
    WebDriverWait(dr, 1).until(lambda x: x.find_element("id", "com.netease.edu.study:id/checkbox_protocol"))
    dr.find_element("id", "com.netease.edu.study:id/checkbox_protocol").click()  # 勾选同意协议
    dr.find_element("id", "com.netease.edu.study:id/login_phone_login").click()  # 手机号登录
    WebDriverWait(dr, 1).until(lambda x: x.find_element("id", "com.netease.edu.study:id/tv_phone_num"))
    dr.find_element("id", "com.netease.edu.study:id/tv_phone_num").send_keys(mobile)  # 输入手机号
    dr.find_element("id", "com.netease.edu.study:id/tv_phone_pwd").send_keys(password)  # 输入密码
    dr.find_element("id", "com.netease.edu.study:id/button").click()  # 点击登录按钮
    # 若有【手机账号安全中心】，则登陆成功
    WebDriverWait(dr, 1).until(lambda x: x.find_element("id", "com.netease.edu.study:id/security_item_name"))
    print("账号登录成功！")


def logout():
    WebDriverWait(dr, 10).until(lambda x: x.find_element("id", "com.netease.edu.study:id/tab_account"))
    dr.find_element("id", "com.netease.edu.study:id/tab_account").click()  # 点击【我的】tab
    WebDriverWait(dr, 1).until(lambda x: x.find_element("id", "com.netease.edu.study:id/security_item_name"))
    os.system("adb shell input swipe 468 1843 468 1200 500")  # 滑动屏幕，显示出【设置】
    WebDriverWait(dr, 1).until(lambda x: x.find_element("id", "com.netease.edu.study:id/settingRl"))
    dr.find_element("id", "com.netease.edu.study:id/settingRl").click()  # 点击设置
    WebDriverWait(dr, 1).until(lambda x: x.find_element("id", "com.netease.edu.study:id/btn_logout"))
    print("点击退出登录")
    dr.find_element("id", "com.netease.edu.study:id/btn_logout").click()  # 点击【退出登录】
    print("已点击退出登录")
    WebDriverWait(dr, 1).until(lambda x: x.find_element("id", "com.netease.edu.study:id/dialog_btn_right"))
    dr.find_element("id", "com.netease.edu.study:id/dialog_btn_right").click()  # 点击弹窗上的退出登录
    os.system("adb shell input swipe 468 1000 468 1600 500")  # 向下滑动屏幕，显示出【设置】
    WebDriverWait(dr, 1).until(lambda x: x.find_element("id", "com.netease.edu.study:id/account_default_text"))
    print("账号已退出")


login("13858008854", "qa123456")
sleep(3)
logout()
