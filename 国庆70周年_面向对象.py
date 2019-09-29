# coding=utf-8
# 导入turtle模块
from turtle import *
# 导入math模块
from math import pi, cos, atan


class Wuxinghongqi:
    def __init__(self, n):
        """
        :param n: 五星红旗的放大倍数，建议为20
        """
        # 设置红旗的长和高
        self.l_g = [i * n for i in [30, 20]]
        # 设置原点的调整位移
        self.x_y = [i * n for i in [-15, 10]]
        # 设置五个星星的外切圆边长
        self.r = [i * n for i in [3, 1, 1, 1, 1]]
        # 设置五个星星的中心点
        self.center = [i * n for j in [(5, -5), (10, -2), (12, -4), (12, -7), (10, -9)] for i in j]
        # 设置五个星星的调整角度
        self.rotation = [0,
                         -(atan(3 / 5) / pi * 180 + 18),
                         atan(3 / 5) / pi * 180 - atan(1 / 6) / pi * 180,
                         atan(1 / 6) / pi * 180 + atan(2 / 7) / pi * 180,
                         atan(4 / 5) / pi * 180 - atan(2 / 7) / pi * 180
                         ]

    # 编写绘制星星的函数
    def start(self, r, x, y, rotation):
        """
        :param r: 包围五角星的圆的半径
        :param x: 五角星的横坐标
        :param y: 五角星的纵坐标
        :param rotation: 调整五角星的角度
        """
        # 由圆的半径求五角星边长
        c = (2 * r ** 2 - 2 * r ** 2 * cos((144 / 180) * pi)) ** (1 / 2)
        pu()
        goto(x, y)
        right(rotation)
        left(162)
        forward(r)
        right(162)
        pd()
        # 填充黄色
        color = (232 / 255, 255 / 255, 8 / 255)
        pencolor(color)
        begin_fill()
        fillcolor(color)
        for i in range(5):
            forward(c)
            right(144)
        end_fill()

    def rec(self, l, g):
        color = (226 / 255, 2 / 255, 18 / 255)  # 红色填充
        pencolor(color)
        begin_fill()
        fillcolor(color)
        for i in range(2):
            forward(l)
            right(90)
            forward(g)
            right(90)
        end_fill()

    def main(self):
        speed(0)
        ht()  # 省略画笔
        pu()
        goto(self.x_y[0], self.x_y[1])
        pd()
        self.rec(self.l_g[0], self.l_g[1])
        for i in range(5):
            self.start(self.r[i],
                       self.center[i * 2] + self.x_y[0],
                       self.center[i * 2 + 1] + self.x_y[1],
                       self.rotation[i])
        done()


if __name__ == "__main__":
    w = Wuxinghongqi(20)
    w.main()
