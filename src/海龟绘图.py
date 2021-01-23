import turtle
import math
from time import sleep

# 定义点的坐标
x1,y1 = 100,100
x2,y2 = 100,-100
x3,y3 = -100,-100
x4,y4 = -100,100

# 开始绘图
turtle.penup()# 抬起笔
turtle.goto(x1,y1)
turtle.pendown()# 放下笔

turtle.goto(x2,y2)
turtle.goto(x3,y3)
turtle.goto(x4,y4)

距离1 = math.sqrt((x1-x2)**2+(y1-y2)**2)
距离2 = math.sqrt((x2-x3)**2+(y2-y3)**2)
距离3 = math.sqrt((x3-x4)**2+(y3-y4)**2)
总距离 = 距离1 + 距离2 + 距离3
turtle.write(总距离)

sleep(3)