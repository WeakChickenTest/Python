#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Author:文晋国
# @DateTime:2020/3/31 11:23
import random

a = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM,.?%$@!'
b = ''
# random.randint()从指定的范围内随机产生一个数，包括上下限
c = random.randint(10, 15)
for i in range(c):
    d = random.randint(0, len(a)-1)
    b = b + a[d]
print(f"密码长度为：{c}")
print(b)

# 912zPspO5DgS
# gitlab密码：4GtKBuzIEpve
# staem密码:UPI8q0xDFg
