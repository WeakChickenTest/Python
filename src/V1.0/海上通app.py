#!/usr/bin/python
# -*- coding: utf-8 -*-

# @Author  : WFT

# @Time    : 2019/9/6 11:41

# @Software: PyCharm

# @FileName: 海上通app.py
import pytest
import yaml
from time import sleep
# with open(file=r"E:\海上通\element\a.yaml",mode='r',encoding='utf-8')as fb:
#   s = yaml.load(fb, Loader=yaml.FullLoader)
from appium import webdriver
d = {
  "platformName": "Android",
  "platformVersion": "5.1.1",
  "deviceName": "emulator-5554",
  "appPackage": "com.grassinfo.android.seapass",
  "appActivity": ".activity.LaunchActivity } in package com.grassinfo.android.seapass",
  "noReset": "true"
}
# 登录app
dr=webdriver.Remote(command_executor='http://127.0.0.1:4723/wd/hub', desired_capabilities=d)
sleep(10)
# dr.find_element_by_id('com.grassinfo.android.seapass:id/tv_new_login').click()
# sleep(10)
# dr.find_element_by_id('com.grassinfo.android.seapass:id/et_phone').click()
# sleep(2)
# dr.find_element_by_id('com.grassinfo.android.seapass:id/et_phone').send_keys('13525038273')
# sleep(2)
# dr.find_element_by_id('com.grassinfo.android.seapass:id/et_password').click()
# dr.find_element_by_id('com.grassinfo.android.seapass:id/et_password').send_keys('wang1995')
# sleep(2)
# dr.find_element_by_id('com.grassinfo.android.seapass:id/iv_login_protocol').click()
# sleep(2)
# dr.find_element_by_id('com.grassinfo.android.seapass:id/tv_login').click()
# sleep(5)
# a=dr.find_element_by_id('com.grassinfo.android.seapass:id/bottom_home_tv').text
# assert  a=='首页'
# print('登录成功')
# sleep(5)

# 进入我的模块
dr.find_element_by_id('com.grassinfo.android.seapass:id/ll_my').click()
sleep(3)
a = dr.find_element_by_id('com.grassinfo.android.seapass:id/tv_editor').text
assert a == '编辑'
print('进入我的模块成功')
sleep(3)
#进入编辑功能
dr.find_element_by_id('com.grassinfo.android.seapass:id/tv_editor').click()
sleep(2)
a=dr.find_element_by_id('com.grassinfo.android.seapass:id/title_tv').text
assert a == '个人资料'
print('进入编辑功能成功')
sleep(2)
dr.find_element_by_id('com.grassinfo.android.seapass:id/ll_nickname').click()
sleep(2)
a= dr.find_element_by_id('com.grassinfo.android.seapass:id/title_tv').text
assert  a == '修改昵称'
print('进入修改昵称界面成功')
sleep(3)
dr.find_element_by_id('com.grassinfo.android.seapass:id/et_nickname').clear()
sleep(2)
test_data = ['wang王qwqwqwq','wan','wan王','wangqwertyuiopasdfg王','wangqwertyuiopasdfg王c']
@pytest.fixture(params=test_data)
def get_data(request):
    return request.param
def test_1(get_data):
    dr.find_element_by_id('com.grassinfo.android.seapass:id/et_nickname').send_keys(test_data[0])
    b = len(4) and len(20)
    assert len(get_data) == b


# # 第一步得到手机屏幕的大小
# s = dr.get_window_size()
# print(s)
# # 第二步 比例缩
# x1=s['width'] * 0.5
# y1=s['height'] * 0.75
# x2=s['width']  * 0.5
# y2=s['height'] * 0.35
#
# # 第三步：滑动
# # dr.swipe(x1,y1,x2,y2)
# def zuohua():
#     dr.swipe(x1,y1,x2,y2)
# zuohua()

# def shanghua():
#     dr.swipe(x2,y2,x2,y1)
# def youhua():
#     dr.swipe(x2,y2,x1,y2)
# def xiahua():
#     dr.swipe(x1,y1,x1,y2)
# dr.get_screenshot_as_base64()  # 截图
# dr.get_screenshot_as_file()  # 图片保存到本机 可以找到保存位置
# dr.get_screenshot_as_png()  # 自动保存
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as Ec
# import selenium.common.exceptions as ex
# from selenium.webdriver.common.by import By
# WebDriverWait(driver=dr,timeout=10,poll_frequency=0.5).until(Ec.presence_of_element_located())
# # Ec.presence_of_element_located 等待某个元素
