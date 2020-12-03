import pygame
from pygame.locals import *
from sys import exit
import numpy as np
from labyrinth import PrimLaby


class Map():
    # 初始化
    def __init__(self, MazeMat):

        # 地图数据: 矩阵、大小、奖励、墙列表、seeker、起始点
        self.mazemat = MazeMat
        self.mazesize = np.shape(self.mazemat)
        self.goal = 0
        self.walls = []  # 墙列表
        for i in range(self.mazesize[0]):
            for j in range(self.mazesize[1]):
                if self.mazemat[i, j] == 0:
                    temp = i, j
                    self.walls.append(temp)
        self.seeker = [0, 0]
        self.start = [0, 0]
        self.end = [self.mazesize[0] - 1, self.mazesize[1] - 1]

    # 根据速度移动
    def stateMove(self, speed):

        # 当返回的速度为0,则移动失败。
        new_seeker = [self.seeker[0] + speed[0], self.seeker[1] + speed[1]]
        # 下一个点是否可用
        if new_seeker[0] < 0 or new_seeker[0] >= self.mazesize[0] or new_seeker[1] < 0 or new_seeker[
            1] >= self.mazesize[1]:
            return (0, 0)
        # 是否撞墙
        if self.mazemat[new_seeker[0], new_seeker[1]] == 0:
            return (0, 0)

        self.seeker = new_seeker
        return speed

    # 是否结束
    def isEnd(self):
        if self.seeker == self.end:
            self.goal += 10
            return True
        else:
            return False

    # 重置起始点
    def reSet(self):
        self.seeker = self.start

    def detector(self):
        print("seeker", self.seeker)
