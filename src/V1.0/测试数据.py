import random
f = open(r'E:\接口\Test.csv','w',encoding = 'utf-8')# a表示在文件末尾追加，w表示先清空文件再写入；encoding表示文件的编码
f.write("a,b,c,d,e\n")# 变量名
a = "0123456789ABCDEF"
b1 = 0
for i in range(10000000):
    b1 = b1+1
    b = ""
    for i in range(8):
        c = random.randint(0, len(a)-1)
        b = b + a[c]
    b = b+","
    for i in range(3):
        for i in range(4):
            c = random.randint(0, len(a)-1)
            b = b + a[c]
        b = b+","
    for i in range(12):
        c = random.randint(0, len(a)-1)
        b = b + a[c]
    f.write(b+"\n")
    print(b)
f.close()# 保存文件