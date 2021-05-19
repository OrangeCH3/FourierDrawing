import turtle as tl
import math


data = []
points = 5000


f = open("datas.txt","r")
for line in f:
    line = eval(line)
    data.append(line)


N = len(data) + 1 # N由上个程序中计算出的级数数量决定，加1是因为有一个角速度为0的量（直流分量）
x = [0] * N
y = [0] * N


# tl.setup(960,720)
tl.penup()
tl.pensize(2) # 画笔粗细
# 三角函数中的值是n * 2 * pi * t , 其中n取0，1，-1，2，-2……，t的范围是[0,1]，当然t取大了没关系，会重复描已经画好的图形
for t in range(points):
    for i in range(len(data)):
        if i % 2 == 0:
            x[i] = data[i][0] * math.cos(i / points * 3.14 * t) - data[i][1] * math.sin(i / points * 3.14 * t)
            y[i] = data[i][0] * math.sin(i / points * 3.14 * t) + data[i][1] * math.cos(i / points * 3.14 * t)


        else:
            x[i] = data[i][0] * math.cos(-(i+1) / points * 3.14 * t) - data[i][1] * math.sin(-(i+1) / points * 3.14 * t)
            y[i] = data[i][0] * math.sin(-(i+1) / points * 3.14 * t) + data[i][1] * math.cos(-(i+1) / points * 3.14 * t)


    tl.goto(int(sum(x))/2, -int(sum(y))/2) # 正负可以控制图形的左右镜像，上下镜像,乘除可以控制缩放
    tl.pendown()