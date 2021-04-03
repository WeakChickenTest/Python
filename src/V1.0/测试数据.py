import random
f = open(r'E:\接口\Test.csv','w',encoding = 'utf-8')# a表示在文件末尾追加，w表示先清空文件再写入；encoding表示文件的编码
f.write("a,b,c,d,e,f,g\n")# 变量名
a1 = "0123456789ABCDEF"# UUID
a2 = "qwertyuiopasdfghjklzxcvbnm"# 名字
a3 = "0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"# 数据
b1 = 0
for i in range(1000):
    b1 = b1+1

    # 用户的UUID
    b = ""
    for i in range(8):
        c = random.randint(0, len(a1)-1)
        b = b + a1[c]
    b = b+","
    for i in range(3):
        for i in range(4):
            c = random.randint(0, len(a1)-1)
            b = b + a1[c]
        b = b+","
    for i in range(12):
        c = random.randint(0, len(a1)-1)
        b = b + a1[c]
    b = b + ","

    # 用户的名字，3~8个字符
    c = random.randint(3,8)
    for i in range(c):
        c1 = random.randint(0, len(a1)-1)
        b = b + a2[c1]
    b = b + ","

    # 年龄
    d = random.randint(20,27)
    b = b + (str(d))

    print(f"第{b1}行数据：{b}")
    f.write(b + "\n")
f.close()# 保存文件
# print(type (b))