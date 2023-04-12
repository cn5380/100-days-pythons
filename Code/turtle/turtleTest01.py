import turtle


turtle.setup(1600,800,0,0)


# 正五角星的角尖是36度，拐度是108度


# ########### 五角星 ###################

turtle.pensize(10)
turtle.pencolor('red')

# turtle.forward(100)
# turtle.left(72)
# turtle.forward(100)
# turtle.right(144)
# turtle.forward(100)
# turtle.left(72)
# turtle.forward(100)
# turtle.right(144)
# turtle.forward(100)
# turtle.left(72)
# turtle.forward(100)
# turtle.right(144)
# turtle.forward(100)
# turtle.left(72)
# turtle.forward(100)
# turtle.right(144)
# turtle.forward(100)
# turtle.left(72)
# turtle.forward(100)
# ########### 五角星 ###################


# ------------- love -------------------
# L
turtle.right(90)
turtle.fd(150)
turtle.left(90)
turtle.fd(80)

# O

turtle.fd(75)
turtle.speed(10)
turtle.circle(60)

# V
turtle.speed(3)
turtle.fd(150)
turtle.left(120)
turtle.fd(120)
turtle.bk(120)
turtle.right(60)
turtle.fd(120)
turtle.bk(120)

# E
turtle.right(60)
turtle.fd(150)

# ------------- love -------------------


turtle.mainloop()








'''1.turtle库的简介

turtle(海龟)库是turtle绘图体系的python实现，turtle库是一种标准库，是python自带的。

turtle(海龟)是一种真实的存在，有一个海龟在窗口的正中心，在画布上游走，走过的轨迹形成了绘制的图形，海龟由程序控制，可改变颜色，宽度等。

2.turtle绘图窗体布局

在电脑上会出现一个窗口，这个是turtle的画布，使用的最小单位是像素；

其中可以通过turtle.(width,height,startx,starty)来设置窗口初始位置及大小。

图片

import turtleturtle.setup(800,800,0,0)

图片

3.turtle的空间坐标体系–(绝对坐标和海龟坐标)

绝对坐标是以屏幕为坐标系，中心位置为(0，0)

图片

可以用turtle.goto(x，y)来让海龟从当前位置走到(x，y)

import turtlefrom time import sleep# turtle.setup(800,800,0,0)turtle.goto(100,100)turtle.goto(100,-100)turtle.goto(-100,-100)turtle.goto(-100,100)turtle.goto(0,0)sleep(5)

图片

另外一种是海龟坐标，是以海龟本身为参考系

图片

turtle.fd(d)表示向海龟前方

turtle.bk(d)表示向海龟后方

turtle.circle(半径,弧度)表示海龟以左侧某一点为圆心的曲线方向

图片


4.turtle的角度坐标体系

绝对坐标：turtle.seth(angle)来改变海龟的游走方向，只改变方向

图片

海龟坐标：

turtle.left(angle),turtle.right(angle)来以海龟为参考系改变方向

图片

实例：

import turtle

turtle.left(45)

turtle.fd(150)

turtle.right(135)

turtle.fd(300)

turtle.left(135)

turtle.fd(150)

图片

5.RGB色彩体系

RGB是由红绿蓝三种颜色通道的颜色组合，每种颜色取值范围是0-255的整数或0-1的小数

系统默认的是小数表示如果想切换成整数，可以使用

turtle.colormode(1.0/255)来变换表示方式

图片

6.turtle画笔控制函数

turtle.penup() #画笔抬起  别名turtle.pu()

turtle.pendown()#画笔降下 别名turtle.pd()

turtle.pensize(宽度) #画笔宽度   

turtle.width(宽度)

turtle.pencolor(color) #画笔颜色  color为字符串 或者 R G B 的值turtle.speed(speed)：设置画笔移动速度，画笔绘制的速度范围[0,10]整数，数字越大越快。

turtle.fillcolor(colorstring) 绘制图形的填充颜色turtle.color(color1,color2)同时设置画笔颜色color1, 填充颜色color2

turtle.pencolor("purple")

turtle.pencolor(0.63,0.13,0.94)

画笔函数抬起和降下一般成对存在，画笔设置后一直有效，直至下次重新设置

7.turtle的运动控制函数

可以控制海龟走直线走曲线

turtle.forward(d) #向前走d个像素，d可以为复数   别名turtle.fd(d)

turtle.circle(r,angle) #根据r绘制angle弧度的弧线     r：默认圆心在海龟左侧r距离的位置 angle：画的角度360内



图片

8.turtle的方向控制函数

turtle.setheading(angle)#改变行进方向            #别名turtle.seth()

turtle.left(angle) #向左转

turtle.right(angle) #向右转

方向控制函数只改变方向，不运动，若让海龟运动需要采用运动控制函数

图片

9.循环语句与range()函数

for   in range  :     循环语句表示每次循环的计数 0 ~ 次数-1

for i in range(5):

   print i

range(N): 产生0到N-1的整数序列共N个

range(M,N) :产生M到N-1个整数序列共N-M个

01234

使用循环可以循环画出图形。

10.画波浪线实例

import turtle from time

import sleep

turtle.setup(650,350,200,200)# 设置屏幕位置

turtle.penup()         #抬起画笔

turtle.fd(-250)      #向后退250(此时不画)

turtle.pendown()       #画笔落下

turtle.pensize(25)     #画笔宽度为25

turtle.pencolor("blue")  #画笔颜色为蓝色

turtle.seth(-40)          #向右转40

for i in range(4):

turtle.circle(40,80) #圆心在左侧半径40 画的弧度为80度(向下弯)   

turtle.circle(-40,80)#圆心在右侧半径40 画的弧度为80度(向上弯)

turtle.done()         #结束绘画后不立即退出，需要手动关闭



turtle.done() 结束绘画后不立即退出，需要手动关闭。

图片


附turte常用操作表

图片



图片

图片

图片'''
