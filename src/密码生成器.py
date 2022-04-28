#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Author:文晋国
# @Time  :2020/3/31 11:23
import random  # 随机模块

a = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM,.?%$@!'
b = ''
c = random.randint(10, 15)  # random.randint 从指定的范围内随机产生一个数，包括上下限

for i in range(c):
    d = random.choice(a)
    b = b + d

print(f"生成的密码为【{b}】,长度是{c}个字符")

# 912zPspO5DgS
# Apple密码：iVaoPDSm04uv
