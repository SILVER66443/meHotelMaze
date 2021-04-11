# 游戏类：由地图类和玩家类构成
from pygame.locals import *
import labyrinth.PrimLaby
import sys
import pygame
import math
import numpy as np

ORANGE = (255, 128, 0)
BLACK = (0, 0, 0)
WIN_SIZE = (1024, 720)
SURF_SIZE = (700, 700)


class Wall(pygame.sprite.Sprite):
    def __init__(self, maze):
        super().__init__()
        self.image = self.create_maze(maze)
        # self.image.set_colorkey(BLACK)
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.top = (WIN_SIZE[1] - SURF_SIZE[1]) / 2
        self.rect.left = (WIN_SIZE[0] - SURF_SIZE[0]) / 2
        self.speed = (2, 2)

    def create_maze(self, maze):
        surf = pygame.surface.Surface(SURF_SIZE)
        matSize = maze.size
        """ 获得墙列表 """
        wallList = []
        mat = maze.getmaze()
        for x in range(matSize[0]):
            for y in range(matSize[1]):
                if mat[x, y] == 255:
                    wallList.append([x, y])
        """ x：层数   y：第几个 """
        for x, y in wallList:
            # x * 这个值用来调整宽度的
            dis = 20 + x * 15
            scale = 660 - x * 30
            arc = 2 * math.pi / matSize[1]
            pos = y * arc
            if (x==0 and y==0) or (x==14 and y==14):
                pygame.draw.arc(surf, [255,255,255], ((dis, dis), (scale, scale)), pos, pos + arc, 10)
            else:
                pygame.draw.arc(surf, ORANGE, ((dis, dis), (scale, scale)), pos, pos + arc, 10)
        return surf


# 初始化 screen
pygame.init()
screen = pygame.display.set_mode(WIN_SIZE)
screen.fill((60, 60, 100))

# 画墙
primmaze = labyrinth.PrimLaby.PrimMaze((15, 15))
mat = primmaze.getmaze()
print(mat)
surface1 = Wall(primmaze)

# walls = [[0, 0], [0, 2],
#          [1, 1], [1, 4],
#          [2, 0], [2, 2],
#          [3, 1], [3, 3]]
# surface1 = Wall((2, 4), walls)

# 帧
clock = pygame.time.Clock()
FPS = 10
running = True
while running:
    clock.tick(FPS)
    """ event detected """
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
    """ 显示 """
    screen.blit(surface1.image, surface1.rect)
    """ 显示FPS """
    text = "FPS: {0:.2f}".format(clock.get_fps())
    pygame.display.set_caption(text)

    # screen.blit(image, (200, 200))
    pygame.display.flip()
