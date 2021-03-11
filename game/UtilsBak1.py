import pygame
from pygame.locals import *
from sys import exit
import numpy as np
from labyrinth import PrimLaby


class Map():
    # 初始化
    def __init__(self, MazeMat):
        # 地图数据: 矩阵、大小、奖励、墙列表、seeker、起始点
        self.puzzle = MazeMat
        self.size = np.shape(self.puzzle)
        self.reward = 0
        self.start = [0, 0]
        self.end = [self.size[0] - 1, self.size[1] - 1]
        self.walls = []  # 墙列表
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                if self.puzzle[i, j] == 0:
                    temp = i, j
                    self.walls.append(temp)


class Player:
    def __init__(self):
        seeker = [0, 0]
        score = 0
        state = 0  # 0:ready 1:playing 2:end


class Game:
    def __init__(self, player, map):
        self.player = player
        self.map = map

    # 根据速度移动
    def state_move(self, speed):

        # 当返回的速度为0,则移动失败。
        new_seeker = [self.seeker[0] + speed[0], self.seeker[1] + speed[1]]
        # 下一个点是否可用
        if new_seeker[0] < 0 or new_seeker[0] >= self.size[0] or new_seeker[1] < 0 or new_seeker[
            1] >= self.size[1]:
            return (0, 0)
        # 是否撞墙
        if self.puzzle[new_seeker[0], new_seeker[1]] == 0:
            return (0, 0)

        self.seeker = new_seeker
        return speed

    # 是否结束
    def is_end(self, state):
        if state == self.end:
            return True
        else:
            return False

    # 重置起始点
    def reset(self):
        self.seeker = self.start

    def detector(self):
        print("seeker", self.seeker)
