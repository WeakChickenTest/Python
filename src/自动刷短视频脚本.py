from random import randint
from time import sleep
import os

a = 0
b = 0

while True:
    c = randint(3,15)# 每个视频在3-15秒之间随机播放
    a = a + 1
    print(f"第{a}次,这个视频观看{c}秒。")
    sleep(c)
    if a>=1000:# 自动播放的数量
        b = b + c
        print(f"当前总共用了{b}秒")
        print("结束!")
        break
    else:
        os.system("adb shell input swipe 527 1594 527 120 100")# 从坐标(527,1594)滑动到坐标(527,120)处，使用100ms时间，模拟人的滑动动作
        b = b + c
        print(f"当前总共用了{b}秒")
sleep(3)
os.system("adb shell am force-stop com.ss.android.ugc.aweme.lite")# 达到播放数量后，自动退出App
"""
while True:
    c = randint(3,30)
    a = a + 1
    print(f"第{a}次,这个视频观看{c}秒。")
    sleep(c)
    if a>=500:
        b = b + c
        print(f"当前总共用了{b}秒")
        print("结束!")
        break
    else:
        os.system("adb shell input swipe 527 1594 527 120 100")
        b = b + c
        print(f"当前总共用了{b}秒")
sleep(3)
os.system("adb shell am force-stop com.kuaishou.nebula")
"""