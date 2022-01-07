#!/usr/bin/python
# -*- coding: UTF-8 -*-
import random

a = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM,.?%$@!'

# 从字符串中随机选择一个字符
b1 = random.choice(a)
print(f"选取的随机字符是:{b1}")

# 从指定范围内随机选一个整数
b2 = random.randint(1, 100)
print(f"选取的随机数字是:{b2}")

# 产生一个0~1之间的浮点数
b3 = random.random()
print(f"选取的随机浮点数是:{b3}")

# 在0~56之间随机选择一个5的倍数
b4 = random.randrange(0, 199, 7)
print(f"选取的随机数字是:{b4}")
