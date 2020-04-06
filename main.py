import random
import time
import turtle
import math

# 调整画笔
turtle.speed(10000)
turtle.pensize(2)
LINE_LENGTH = 15
class MyPen:
    '''
    一只笔
    '''
    def __init__(self):
        self.pen_x, self.pen_y = 0, 0
    def goto(self, to_x, to_y):
        '''
        让画笔移动到某一点
        '''
        if (self.pen_x, self.pen_y) == (to_x, to_y):
            return
        turtle.penup()
        turtle.goto(to_x, to_y)
        turtle.pendown()
        self.pen_x, self.pen_y = to_x, to_y
    def draw(self, to_x, to_y):
        '''
        让画笔画到某一点
        '''
        if (self.pen_x, self.pen_y) == (to_x, to_y):
            return
        turtle.goto(to_x, to_y)
        self.pen_x, self.pen_y = to_x, to_y

PEN = MyPen()

class dot:
    __slots__ = ("x", "y", "z")
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __eq__(self, obj):
        return self.x == obj.x and self.y == obj.y and self.z == obj.z
    def __hash__(self):
        return self.x ^ self.y ^ self.z
    def __lt__(self, obj):
        return self.x + self.y + self.z < obj.x + obj.y + obj.z
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
        PEN.goto(px, py)
        turtle.circle(1, 360)


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
        return self.dot1.__hash__() * self.dot2.__hash__()
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
        PEN.goto(x, y)
        x, y = self.dot2.toTwo()
        PEN.draw(x, y)

class cube:
    __slots__ = ("dot_a", "dot_b", "dot_c", "dot_d",\
                "dot_a1", "dot_b1", "dot_c1", "dot_d1", "lines")
    def __init__(self, dot1, dot2):
        self.dot_a, self.dot_c1 = dot1, dot2
        self.dot_b = dot(self.dot_c1.x, self.dot_a.y, self.dot_a.z)
        self.dot_c = dot(self.dot_c1.x, self.dot_c1.y, self.dot_a.z)
        self.dot_d = dot(self.dot_a.x, self.dot_c1.y, self.dot_a.z)
        self.dot_a1 = dot(self.dot_a.x, self.dot_a.y, self.dot_c1.z)
        self.dot_b1 = dot(self.dot_c1.x, self.dot_a.y, self.dot_c1.z)
        self.dot_d1 = dot(self.dot_a.x, self.dot_c1.y, self.dot_c1.z)
        self.lines = [
        line(self.dot_a, self.dot_b),
        line(self.dot_b, self.dot_c),
        line(self.dot_c, self.dot_d),
        line(self.dot_d, self.dot_a),
        line(self.dot_d, self.dot_d1),
        line(self.dot_c, self.dot_c1),
        line(self.dot_b, self.dot_b1),
        line(self.dot_a, self.dot_a1),
        line(self.dot_a1, self.dot_b1),
        line(self.dot_b1, self.dot_c1),
        line(self.dot_c1, self.dot_d1),
        line(self.dot_d1, self.dot_a1),
        ]
    def __lt__(self, obj):
        return self.dot_a < obj.dot_a
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
], [#1
    "   *",
    "  **",
    "   *",
    "   *",
    "   *",
], [#2
    " ** ",
    "   *",
    "  * ",
    " *  ",
    " ***",
], [#3
    "*** ",
    "   *",
    " ** ",
    "   *",
    "*** ",
], [#4
    "*   ",
    "*  *",
    "****",
    "   *",
    "   *",
], [#5
    "****",
    "*   ",
    "****",
    "   *",
    "*** ",
], [#6
    " ** ",
    "*   ",
    "*** ",
    "* * ",
    " ** ",
], [#7
    " ***",
    "   *",
    "  * ",
    " *  ",
    " *  ",
], [#8
    " ** ",
    "*  *",
    " ** ",
    "*  *",
    " ** ",
], [#9
    " ***",
    " * *",
    " ***",
    "   *",
    " ** ",
]]

word_to_pixels = [[#A
    " ** ",
    "*  *",
    "****",
    "*  *",
    "*  *",
], [#B
    "*** ",
    "*  *",
    "*** ",
    "*  *",
    "*** ",
], [#C
    " ** ",
    "*   ",
    "*   ",
    "*   ",
    " ** ",
], [#D
    "*** ",
    "*  *",
    "*  *",
    "*  *",
    "*** ",
], [#E
    "***",
    "*  ",
    "** ",
    "*  ",
    "***",
], [#F
    "***",
    "*  ",
    "** ",
    "*  ",
    "*  ",
], [#G
    " ** ",
    "*   ",
    "* **",
    "*  *",
    " ** ",
], [#H
    "*  *",
    "*  *",
    "****",
    "*  *",
    "*  *",
], [#I
    "***",
    " * ",
    " * ",
    " * ",
    "***",
], [#J
    "  *",
    "  *",
    "  *",
    "* *",
    " * ",
], [#K
    "* *",
    "* *",
    "** ",
    "* *",
    "* *",
], [#L
    "*  ",
    "*  ",
    "*  ",
    "*  ",
    "***",
], [#M
    "*   *",
    "** **",
    "* * *",
    "*   *",
    "*   *",
], [#N
    "*  *",
    "** *",
    "* **",
    "*  *",
    "*  *",
], [#O
    " ** ",
    "*  *",
    "*  *",
    "*  *",
    " ** ",
], [#P
    "*** ",
    "*  *",
    "*** ",
    "*   ",
    "    ",
], [#Q
    " ** ",
    "*  *",
    "*  *",
    "* **",
    " ***",
], [#R
    "*** ",
    "*  *",
    "*** ",
    "*  *",
    "*  *",
], [#S
    " ***",
    "*   ",
    " ** ",
    "   *",
    "*** ",
], [#T
    "****",
    " *  ",
    " *  ",
    " *  ",
    " *  ",
], [#U
    "*  *",
    "*  *",
    "*  *",
    "*  *",
    " ** ",
], [#V
    "*  *",
    "*  *",
    "*  *",
    " ** ",
    "  * ",
], [#W
    "*   *",
    "*   *",
    "*   *",
    "* * *",
    " * * ",
], [#X
    "*   *",
    " * * ",
    "  *  ",
    " * * ",
    "*   *",
], [#Y
    "*   *",
    " * * ",
    "  *  ",
    "  *  ",
    "  *  ",
], [#Z
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
    return sorted(cubes)

def numsToCube(n:str, *, length = 20, offset = dot(0, 0, 0)):
    '''
    将数字以及字母转变为方块

    使用offset
    '''
    n = n.upper()
    len_pixel = 0
    for i in n:
        if 48 <= ord(i) <= 57:
            pix = numToPixels[ord(i)-48]
        elif 65 <= ord(i) <= 90:
            pix = word_to_pixels[ord(i)-65]
        else:
            pix = spacePixels
        len_pixel += len(pix[0])
    dotLD = dot(-len_pixel//2 * length + offset.x, offset.y, offset.z)
    cubes = []
    for i in n:
        if 48 <= ord(i) <= 57:
            pix = numToPixels[ord(i)-48]
        elif 65 <= ord(i) <= 90:
            pix = word_to_pixels[ord(i)-65]
        else:
            pix = spacePixels
        cubes += pixelsToCube(pix, dotLD, length)
        dotLD = dot(dotLD.x + length * (len(pix[0])+1), dotLD.y, dotLD.z)
    return cubes

def drawCubes(cubes: list):
    lines = []
    for cu in cubes:
        for line in cu.lines:
            if line in lines:
                continue
            for i in range(1, len(lines)-1):
                if line.dot1 == lines[i].dot2 and lines[i+1].dot1 != lines[i].dot2:
                    lines.insert(i+1, line)
                    break
            else:
                lines.append(line)
    for line in lines:
        line.draw()

def write_str(write_str):
    length = LINE_LENGTH
    line_num = 0
    write_strs = write_str.split("\n")
    for i in write_strs:
        drawCubes(numsToCube(i, length=length,\
            offset=dot(0, 0, length * 7 * (len(write_strs)//2 - line_num))))
        line_num += 1

if __name__ == "__main__":
    turtle.setup(0.8, 0.8)
    s = "what\ndo\nyou\nthink"
    t1 = time.time()
    write_str(s)
