# 随机prim算法
# 缺少思想：点变动的时候添加墙
import numpy as np
from matplotlib import pyplot as plt
import random
import matplotlib.cm as cm


class PrimMaze():
    def __init__(self, mazesize):
        self.image = np.array([])  # 类型备份，因为后面我需要迷宫成2值状态
        self.size = mazesize  # 大小
        self.maze = self.initmaze()  # 初始化迷宫矩阵规格
        self.seeker = self.initseeker(mazesize)  # 初始化Seeker
        self._walls = []  # 墙列表
        self.createmaze()  # 生成迷宫

    # 初始化规格
    def initmaze(self):

        x, y = self.size
        maze = np.zeros(self.size)  # 创建0矩阵
        # 标记墙
        for i in range(x):
            for j in range(y):
                if i % 2 == 1 or j % 2 == 1:
                    maze[i, j] = 1
        return maze

    # 初始化seeker
    def initseeker(self, size):
        self.maze[int((size[0] + 1) / 2), int((size[1] + 1) / 2)] = 2
        return int((size[0] + 1) / 2), int((size[1] + 1) / 2)

    # 将墙插入列表
    def insertwall(self):
        size = np.shape(self.maze)

        # 添加过程
        if self.seeker[0] + 1 < size[0] and self.maze[self.seeker[0] + 1, self.seeker[1]] == 1:
            self._walls.append((self.seeker[0] + 1, self.seeker[1]))
        if self.seeker[0] - 1 > 0 and self.maze[self.seeker[0] - 1, self.seeker[1]] == 1:
            self._walls.append((self.seeker[0] - 1, self.seeker[1]))
        if self.seeker[1] + 1 < size[1] and self.maze[self.seeker[0], self.seeker[1] + 1] == 1:
            self._walls.append((self.seeker[0], self.seeker[1] + 1))
        if self.seeker[1] - 1 > 0 and self.maze[self.seeker[0], self.seeker[1] - 1] == 1:
            self._walls.append((self.seeker[0], self.seeker[1] - 1))

        # 使用集合得特性去掉重复得墙
        self._walls = list(set(self._walls))

    # 摧毁墙
    def destroywall(self, wall):
        x = wall[0]
        y = wall[1]

        # 纵墙
        if wall[0] % 2 == 1:
            # 上边和下边都访问过，无效墙
            if self.maze[x - 1, y] == 2 and self.maze[x + 1, y] == 2:
                self.maze[x, y] = 3
                return True
            # 穿透
            else:
                self.maze[x, y] = 2
                if self.maze[x - 1, y] == 2:
                    self.maze[x + 1, y] = 2
                    self.seeker = (x + 1, y)
                    return True
                elif self.maze[x + 1, y] == 2:
                    self.maze[x - 1, y] = 2
                    self.seeker = (x - 1, y)
                    return True
        # 横墙
        if wall[1] % 2 == 1:
            # 左边和右边都访问过，无效墙
            if self.maze[x, y - 1] == 2 and self.maze[x, y + 1] == 2:
                self.maze[x, y] = 3
                return True
            # 穿透
            else:
                self.maze[x, y] = 2
                if self.maze[x, y - 1] == 2:
                    self.maze[x, y + 1] = 2
                    self.seeker = (x, y + 1)
                    return True
                elif self.maze[x, y + 1] == 2:
                    self.maze[x, y - 1] = 2
                    self.seeker = (x, y - 1)
                    return True
        print(wall, "invalid wall , can not destroy!")
        return False

    # 将迷宫初始化
    def createmaze(self):
        while True:
            self.insertwall()
            temp = self._walls.pop(random.randint(0, np.shape(self._walls)[0] - 1))
            self.destroywall(temp)
            if not self._walls:
                break

    # 返回迷宫序列
    def displaymaze(self):
        return self.image

    # 返回2值矩阵，用于画图等等
    def getmaze(self):
        self.image = self.maze
        for i in range(0, self.size[0]):
            for j in range(0, self.size[1]):
                if self.image[i, j] == 2:
                    self.image[i, j] = 255
                if self.image[i, j] == 1 or self.image[i, j] == 3:
                    self.image[i, j] = 0
        return self.image

    def dispaly1(self):
        plt.imshow(self.maze, cmap=cm.Greys_r, interpolation='none')
        plt.show()


