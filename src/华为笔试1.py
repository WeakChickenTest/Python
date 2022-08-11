"""
若干个大于等于1，小于等于100的整数，分成n份，每一份里的所有数字都可以被这里边最小数字整除。
要求给出一组数字，计算出可以分成几份
"""

# 先将输入的内容变成列表
a = eval(input("请输入数组："))
b = list(a)

# 将列表的元素按照从小到大的顺序排列
# [10, 45, 17, 55, 49, 72, 56, 33, 7, 12, 35, 53, 81, 27, 49]
for i in range(len(b)):
    for j in range(len(b)):
        if b[i] < b[j]:
            b[i], b[j] = b[j], b[i]
print(b)

c = []
c1 = []
for i in b:
    d = []
    for j in b:
        # 分别取出列表中的数字，令列表中的元素进行取余运算，已经有过取余为0的数字不再参与取余运算
        if j % i == 0 & j not in c1:
            d.append(j)
            c1.append(j)
    c.append(d)
# 删除空的列表
n = 0
for i in c:
    if len(i) == 0:
        n = n + 1
for m in range(n):
    c.remove([])
# 输出分组结果和所需要的颜色数量
print(c)
print(len(c))
