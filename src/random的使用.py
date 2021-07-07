#!/usr/bin/python
# -*- coding: UTF-8 -*-
import random

a = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM,.?%$@!'
b1 = random.choice(a)# 从字符串中随机选择一个字符
b2 = random.randint(1, 100)# 从指定范围内随机选一个整数
b3 = random.random()# 产生一个0~1之间的浮点数
b4 = random.randrange(0, 56, 5)# 在0~56之间随机选择一个5的倍数
print(b4)