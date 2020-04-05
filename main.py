import random
import time
import turtle
import math

# 调整画笔
turtle.speed(3)
turtle.pensize(3)

class MyPen:
    def __init__(self):
        self.x, self.y = 0, 0
    def goto(self, x, y):
        if (self.x, self.y) == (x, y):
            return
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        self.x, self.y = x, y
    def draw(self, x, y):
        if (self.x, self.y) == (x, y):
            return
        turtle.goto(x, y)
        self.x, self.y = x, y

pen = MyPen()

class dot:
    __slots__ = ("x", "y", "z")
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __eq__(self, obj):
        return self.x == obj.x and self.y == obj.y and self.z == obj.z
    def __hash__(self):
        return self.x + self.y + self.z
    def toTwo(self):
        '''
        将一个三维点转变为二维坐标
        '''
        return (self.x-self.y//2, self.z-self.y//2)
    def draw(self):
        '''
        点一个点
        '''
        px, py = self.toTwo()
        
        turtle.circle(1, 360)
        is_pen_down == True

class line:
    __slots__ = ("dot1", "dot2", "len")
    def __init__(self, dot1, dot2):
        self.dot1 = dot1
        self.dot2 = dot2
        self.len = math.sqrt((self.dot1.x-self.dot2.x)**2 +\
                            (self.dot1.y-self.dot2.y)**2 +\
                            (self.dot1.z-self.dot2.z)**2)
    def __eq__(self, obj):
        return self.dot1 == obj.dot1 and self.dot2 == obj.dot2
    def __hash__(self):
        return self.dot1.__hash__() + self.dot2.__hash__()
    def __lt__(self,obj):
        if self.len != obj.len:
            return self.len < obj.len
        else:
            return self.dot1.x + self.dot1.y + self.dot1.z < obj.dot1.x + obj.dot1.y + obj.dot1.z
    def draw(self):
        '''
        画出一条线
        '''
        x, y = self.dot1.toTwo()
        pen.goto(x, y)
        x, y = self.dot2.toTwo()
        pen.draw(x, y)

class cube:
    __slots__ = ("A", "B", "C", "D", "A1", "B1", "C1", "D1", "lines")
    def __init__(self, dot1, dot2):
        self.A, self.C1 = dot1, dot2
        self.B = dot(self.C1.x, self.A.y, self.A.z)
        self.C = dot(self.C1.x, self.C1.y, self.A.z)
        self.D = dot(self.A.x, self.C1.y, self.A.z)
        self.A1 = dot(self.A.x, self.A.y, self.C1.z)
        self.B1 = dot(self.C1.x, self.A.y, self.C1.z)
        self.D1 = dot(self.A.x, self.C1.y, self.C1.z)
        self.lines = [
        line(self.A, self.B),
        line(self.B, self.C),
        line(self.C, self.D),
        line(self.D, self.A),
        line(self.D, self.D1),
        line(self.C, self.C1),
        line(self.B, self.B1),
        line(self.A, self.A1),
        line(self.A1, self.B1),
        line(self.B1, self.C1),
        line(self.C1, self.D1),
        line(self.D1, self.A1),
        ]
    def draw(self):
        '''
        画出这个方块
        '''
        for i in self.lines:
            i.draw()

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
                cubes.append(cube(dot1, dot2))
    for i in range(1, len(cubes)-1):
        for j in range(i+2, len(cubes)):
            if line(cubes[i].A, cubes[j].A).len < line(cubes[i].A, cubes[i+1].A).len:
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

def drawCubes(cubes: list):
    '''
    lines = set()
    for cu in cubes:
        for line in cu.lines:
            lines.add(line)
    for line in sorted(list(lines)):
        line.draw()
    '''
    lines = []
    for cu in cubes:
        for line in cu.lines:
            if line in lines:
                continue
            for i in range(len(lines)-1):
                if line.dot1 == lines[i].dot2 and lines[i+1].dot1 != lines[i].dot2:
                    lines.insert(i+1, line)
                    break
            else:
                lines.append(line)
    for line in lines:
        line.draw()

t1 = time.time()
drawCubes(numsToCube("abc", length=20, offset=dot(0, 0, -120)))
print(time.time()-t1)
t1 = time.time()
for cu in numsToCube("abc", length=20):
    cu.draw()
print(time.time()-t1)
time.sleep(2)