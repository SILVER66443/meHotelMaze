# 随机prim算法
# 缺少思想：点变动的时候添加墙
import numpy as np
from matplotlib import pyplot as plt
import random
import matplotlib.cm as cm

class prim_Maze():
    def __init__(self):
        self.image=np.array([])
        self.maze = self.initMaze()
        self.size = np.shape(self.maze)
        self.seeker = self.initSeeker()
        self._walls = []
        self.createMaze()

    # 初始化规格
    def initMaze(self):
        x = 9
        y = 9
        size = x, y
        maze = np.zeros(size)
        for i in range(x):
            for j in range(y):
                if i % 2 == 1 or j % 2 == 1:
                    maze[i, j] = 1
        return maze

    # 初始化seeker
    def initSeeker(self):
        self.maze[0, 0] = 2
        return (0, 0)

    #将墙插入列表
    def insertWall(self):
        size = np.shape(self.maze)

        if self.seeker[0] + 1 < size[0] and self.maze[self.seeker[0] + 1, self.seeker[1]] == 1:
            self._walls.append((self.seeker[0] + 1, self.seeker[1]))
        if self.seeker[0] - 1 > 0 and self.maze[self.seeker[0] - 1, self.seeker[1]] == 1:
            self._walls.append((self.seeker[0] - 1, self.seeker[1]))
        if self.seeker[1] + 1 < size[1] and self.maze[self.seeker[0], self.seeker[1] + 1] == 1:
            self._walls.append((self.seeker[0], self.seeker[1] + 1))
        if self.seeker[1] - 1 > 0 and self.maze[self.seeker[0], self.seeker[1] - 1] == 1:
            self._walls.append((self.seeker[0], self.seeker[1] - 1))
        self._walls = list(set(self._walls))

    # 摧毁墙
    def destroy(self, wall):
        x = wall[0]
        y = wall[1]

        # 纵墙
        if wall[0] % 2 == 1:
            # 上边和下边都访问过，无效墙
            if self.maze[x - 1, y] == 2 and self.maze[x + 1, y] == 2:
                self.maze[x,y]=3
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
        print(wall,"invalid wall , can not destroy!")
        return False

    #将迷宫初始化，
    def createMaze(self):
        while True:
            self.insertWall()
            temp = self._walls.pop(random.randint(0, np.shape(self._walls)[0] - 1))
            self.destroy(temp)
            if self._walls == []:
                break
    # 返回迷宫序列
    def displayMaze(self):
        return self.image
    # 画图看一下
    def getImage(self):
        self.image = self.maze
        for i in range(0, self.size[0]):
            for j in range(0, self.size[1]):
                if self.image[i, j] == 2:
                    self.image[i, j] = 255
                if self.image[i, j] == 1 or self.image[i, j] == 3:
                    self.image[i, j] = 0

        #plt.imshow(self.image, interpolation='none')
        #plt.show()
        return self.image

# main process
maze1 = prim_Maze()
maze1.getImage()
maze1.displayMaze()

