#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Author:文晋国
# @Time  :2020/3/31 11:23
import random # 随机模块
a = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'#,.?%$@!
b = ''
c = random.randint(9,12) # random.randint 从指定的范围内随机产生一个数，包括上下限
for i in range(c):
    d = random.randint(0,len(a)-1)
    b = b + a[d]
print(c)
print(b)

# 912zPspO5DgS