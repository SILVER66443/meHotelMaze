import pygame
from pygame.locals import *
from sys import exit
import numpy as np
from labyrinth import prim_self

class Map():
    # 初始化
    def __init__(self, MazeMat):
        # 地图数据
        self.maze = MazeMat
        self.size = np.shape(self.maze)
        # 墙列表
        self.wall_list = []
        print(self.size)
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                if self.maze[i, j] == 0:
                    temp = i, j
                    self.wall_list.append(temp)
        # seeker初始位置和可调度的速度
        self.seeker = [0, 0]
        self.step = [0, 0]
        # 起点终点
        self.start = [0, 0]
        self.end = [self.size[0] - 1, self.size[1] - 1]

    # 设置速度
    def set_step(self, step):
        self.step = step

    # 根据速度移动
    def move(self):
        new_seeker = [self.seeker[0] + self.step[0], self.seeker[1] + self.step[1]]

        if new_seeker[0] < 0 or new_seeker[0] >= self.size[0] or new_seeker[1] < 0 or new_seeker[
            1] >= self.size[1]:
            return [0, 0]
        if self.maze[new_seeker[0], new_seeker[1]] == 0:

            return [0, 0]

        self.seeker = new_seeker
        return self.step

    # 是否结束
    def is_end(self):
        if self.seeker == self.end:
            return True

    # 重置起始点
    def reset(self):
        self.seeker = self.start

    def detector(self):
        print("seeker", self.seeker)
        print("step", self.step)

