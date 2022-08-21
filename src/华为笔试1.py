"""
若干个大于等于1，小于等于100的整数，分成n份，每一份里的所有数字都可以被这里边最小数字整除。
要求：给出一组数字，计算出可以分成几份
"""
import random

int0 = int(input("请输入大于等于1，小于等于100的整数："))

list1 = []
while True:
    int1 = random.randint(1, 100)
    # 随机数不在列表中，就添加到里边
    if int1 not in list1:
        list1.append(int1)

    # 如果列表长度达到了要求，就跳出循环
    if len(list1) == int0:
        break

# 按照从小到大的顺序排列
for l1 in range(len(list1)):
    for l2 in range(len(list1)-1):
        if list1[l1] < list1[l2]:
            list1[l1], list1[l2] = list1[l2], list1[l1]

a1 = []
a2 = []
for j1 in list1:
    a3 = []
    for j2 in list1:
        if j2 not in a2 and j2 % j1 == 0:
            a2.append(j2)
            a3.append(j2)
    a1.append(a3)

A = []
for L in a1:
    if len(L) != 0:
        A.append(L)
print(len(A))
print(A)
