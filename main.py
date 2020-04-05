import random
import time
import turtle
import math

# 调整画笔
turtle.speed(2000)
turtle.pensize(3)

class dot:
    __slots__ = ("x", "y", "z")
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def toTwo(self):
        '''
        将一个三维点转变为二维坐标
        '''
        return (self.x-self.y//2, self.z-self.y//2)
    def draw(self):
        '''
        点一个点
        '''
        turtle.penup()
        x, y = self.toTwo()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.circle(1, 360)

class line:
    __slots__ = ("dot1", "dot2")
    def __init__(self, dot1, dot2):
        self.dot1 = dot1
        self.dot2 = dot2

    def draw(self):
        '''
        画出一条线
        '''
        turtle.penup()
        x, y = self.dot1.toTwo()
        turtle.goto(x, y)
        turtle.pendown()
        x, y = self.dot2.toTwo()
        turtle.goto(x, y)
    def len(self):
        return math.sqrt((self.dot1.x-self.dot2.x)**2 + (self.dot1.y-self.dot2.y)**2 + (self.dot1.z-self.dot2.z)**2)

class cube:
    __slots__ = ("A", "B", "C", "D", "A1", "B1", "C1", "D1")
    def __init__(self, dot1, dot2):
        self.A, self.C1 = dot1, dot2
        self.B = dot(self.C1.x, self.A.y, self.A.z)
        self.C = dot(self.C1.x, self.C1.y, self.A.z)
        self.D = dot(self.A.x, self.C1.y, self.A.z)
        self.A1 = dot(self.A.x, self.A.y, self.C1.z)
        self.B1 = dot(self.C1.x, self.A.y, self.C1.z)
        self.D1 = dot(self.A.x, self.C1.y, self.C1.z)
    def draw(self):
        '''
        画出这个方块
        '''
        line(self.A, self.B).draw()
        line(self.B, self.C).draw()
        line(self.C, self.D).draw()
        line(self.D, self.A).draw()
        line(self.D, self.D1).draw()
        line(self.C, self.C1).draw()
        line(self.B, self.B1).draw()
        line(self.A, self.A1).draw()
        line(self.A1, self.B1).draw()
        line(self.B1, self.C1).draw()
        line(self.C1, self.D1).draw()
        line(self.D1, self.A1).draw()

#像素形式的数字
numToPixels = [[#0
    " ** ",
    "* **",
    "** *",
    "** *",
    " ** ",
],[#1
    "   *",
    "  **",
    "   *",
    "   *",
    "   *",
],[#2
    " ** ",
    "   *",
    "  * ",
    " *  ",
    " ***",
],[#3
    "*** ",
    "   *",
    " ** ",
    "   *",
    "*** ",
],[#4
    "*   ",
    "*  *",
    "****",
    "   *",
    "   *",
],[#5
    "****",
    "*   ",
    "****",
    "   *",
    "*** ",
],[#6
    " ** ",
    "*   ",
    "*** ",
    "* * ",
    " ** ",
],[#7
    " ***",
    "   *",
    "  * ",
    " *  ",
    " *  ",
],[#8
    " ** ",
    "*  *",
    " ** ",
    "*  *",
    " ** ",
],[#9
    " ***",
    " * *",
    " ***",
    "   *",
    " ** ",
]]

wordToPixels = [[#A
    " ** ",
    "*  *",
    "****",
    "*  *",
    "*  *",
],[#B
    "*** ",
    "*  *",
    "*** ",
    "*  *",
    "*** ",
],[#C
    " ** ",
    "*   ",
    "*   ",
    "*   ",
    " ** ",
],[#D
    "*** ",
    "*  *",
    "*  *",
    "*  *",
    "*** ",
],[#E
    "***",
    "*  ",
    "** ",
    "*  ",
    "***",
],[#F
    "***",
    "*  ",
    "** ",
    "*  ",
    "*  ",
],[#G
    " ** ",
    "*   ",
    "* **",
    "*  *",
    " ** ",
],[#H
    "*  *",
    "*  *",
    "****",
    "*  *",
    "*  *",
],[#I
    "***",
    " * ",
    " * ",
    " * ",
    "***",
],[#J
    "  *",
    "  *",
    "  *",
    "* *",
    " * ",
],[#K
    "* *",
    "* *",
    "** ",
    "* *",
    "* *",
],[#L
    "*  ",
    "*  ",
    "*  ",
    "*  ",
    "***",
],[#M
    "*   *",
    "** **",
    "* * *",
    "*   *",
    "*   *",
],[#N
    "*  *",
    "** *",
    "* **",
    "*  *",
    "*  *",
],[#O
    " ** ",
    "*  *",
    "*  *",
    "*  *",
    " ** ",
],[#P
    "*** ",
    "*  *",
    "*** ",
    "*   ",
    "    ",
],[#Q
    " ** ",
    "*  *",
    "*  *",
    "* **",
    " ***",
],[#R
    "*** ",
    "*  *",
    "*** ",
    "*  *",
    "*  *",
],[#S
    " ***",
    "*   ",
    " ** ",
    "   *",
    "*** ",
],[#T
    "****",
    " *  ",
    " *  ",
    " *  ",
    " *  ",
],[#U
    "*  *",
    "*  *",
    "*  *",
    "*  *",
    " ** ",
],[#V
    "*  *",
    "*  *",
    "*  *",
    " ** ",
    "  * ",
],[#W
    "*   *",
    "*   *",
    "*   *",
    "* * *",
    " * * ",
],[#X
    "*   *",
    " * * ",
    "  *  ",
    " * * ",
    "*   *",
],[#Y
    "*   *",
    " * * ",
    "  *  ",
    "  *  ",
    "  *  ",
],[#Z
    "*****",
    "  *  ",
    " *   ",
    "*    ",
    "*****",
]]

spacePixels = [
    "    ",
    "    ",
    "    ",
    "    ",
    "    ",
]

def pixelsToCube(pixels, dotLD, length):
    '''
    将像素转变为方块
    '''
    cubes = []
    for i in range(len(pixels)):
        for j in range(len(pixels[i])):
            if pixels[i][j] != " ":
                dot1 = dot(dotLD.x + j * length, dotLD.y, dotLD.z + (len(pixels)-i) * length)
                dot2 = dot(dot1.x + length, dot1.y + length, dot1.z + length)
                cube1 = cube(dot1, dot2)
                cubes.append(cube1)
    for i in range(1, len(cubes)-1):
        for j in range(i+2, len(cubes)):
            if line(cubes[i].A, cubes[j].A).len() < line(cubes[i].A, cubes[i+1].A).len():
                cubes[j], cubes[i+1] = cubes[i+1], cubes[j]
    return cubes

def numsToCube(n:str, *, length = 20, dotLD = None, offset = dot(0, 0, 0)):
    '''
    将数字以及字母转变为方块

    如果提供了dotLD则使用dotLD，否则使用offset
    '''
    n = n.upper()
    if dotLD == None:
        dotLD = dot(-len(n)//2 * length * 5 + offset.x, offset.y, offset.z)
    cubes = []
    for i in n:
        if 48<=ord(i)<=57:
            pix = numToPixels[ord(i)-48]
        elif 65<=ord(i)<=90:
            pix = wordToPixels[ord(i)-65]
        else:
            pix = spacePixels
        cubes += pixelsToCube(pix, dotLD, length)
        dotLD = dot(dotLD.x + length * (len(pix[0])+1), dotLD.y, dotLD.z)
    return cubes

for cu in numsToCube("abcde", length = 20):
    cu.draw()  
time.sleep(2)
