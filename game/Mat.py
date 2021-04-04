# 地图类：包含地图初始化数据、奖励目标、结束判断位置等等属于地图才有的属性


import numpy as np
import random
from labyrinth import PrimLaby


class Mat:
    # 初始化
    def __init__(self, MazeMat):
        """ 地图数据: 矩阵、大小、奖励、墙列表、seeker、起始点 """

        # 地图、大小、起始点
        self.puzzle = MazeMat
        self.size = np.shape(self.puzzle)
        self.start = [0, 0]
        self.end = [self.size[0] - 1, self.size[1] - 1]

        # 墙列表
        self.walls = []
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                if self.puzzle[i, j] == 0:
                    self.walls.append((i, j))

        # 奖励点
        self.gold = []
        i = 0
        while i < 10:
            x = random.randint(0, self.size[0])
            y = random.randint(0, self.size[1])
            if (x, y) not in self.walls:
                self.gold.append((x, y))
                i += 1

    def getstate(self, pos):
        """ 判断pos点是什么类型 """
        pos = tuple(pos)
        if pos == self.end:
            return "end"
        elif pos in self.gold:
            self.gold.remove(pos)
            return "gold"
        elif pos in self.walls:
            return "wall"
        else:
            return "pass"

    def get_info(self):
        """ 输出类的信息 """
        print("地图：")
        print(self.puzzle)
        print("大小")
        print(self.size)
        print("奖励：")
        print(self.gold)
        print("start:", self.start, "end:", self.end)
        print("墙")
        print(self.walls)


mat1 = Mat(PrimLaby.PrimMaze((15, 15)).getmaze())
print(mat1.get_info())