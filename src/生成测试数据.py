import random


f = open(r"Test.txt", "w", encoding="utf-8")  # 指定文件位置和编码方式
f.write("A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,1,2,3,4\n")  # 写入第一行的变量，最后换行\n
a = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
# 总的数据量
for i in range(5000):
    for j in range(9):
        b1 = ""
        c1 = random.randint(10, 20)
        for k in range(c1):
            d1 = random.choice(a)
            b1 = b1+d1
        f.write(f'{b1},')
    c2 = random.randint(10, 20)
    b2 = ""
    for k in range(c2):
        d2 = random.choice(a)
        b2 = b2 + d2
    f.write(f'{b2}\n')

    print(f"第{i+1}行数据")

# 所有数据写入后保存文件
f.close()
