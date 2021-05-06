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


# 地图
class Wall(pygame.sprite.Sprite):
    def __init__(self, maze):
        super().__init__()
        self.image = self.create_maze(maze)
        self.image.set_colorkey(BLACK)
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
            if (x == 0 and y == 0) or (x == 14 and y == 14):
                pygame.draw.arc(surf, [255, 255, 255], ((dis, dis), (scale, scale)), pos, pos + arc, 7)
            else:
                pygame.draw.arc(surf, ORANGE, ((dis, dis), (scale, scale)), pos, pos + arc, 7)
        return surf


# seeker
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("G:/pyProject/meHotelMaze/PNG/seeker.png")
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.image.set_colorkey(BLACK)
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.top = 0
        self.rect.left = WIN_SIZE[0] / 2
        self.speed = (0, 2)

    def move(self):
        self.rect = self.rect.move(self.speed)


""" *** """
# 初始化 screen
pygame.init()
screen = pygame.display.set_mode(WIN_SIZE)
screen.fill((60, 60, 100))
ball = Ball()

# 画墙
primmaze = labyrinth.PrimLaby.PrimMaze((15, 15))
mat = primmaze.getmaze()
print(mat)
surface1 = Wall(primmaze)

# 帧
clock = pygame.time.Clock()
FPS = 50
running = True
angle = 1
delta = 1
while running:
    clock.tick(FPS)
    """ event detected """
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                delta = 0 - delta

    """ 旋转 """
    newimage = pygame.transform.rotate(surface1.image, angle)
    newrect = newimage.get_rect(center=surface1.rect.center)
    angle += delta
    if angle == 360 or angle == -360:
        angle = 0

    """ 显示 """
    screen.fill((60, 60, 100))
    screen.blit(newimage, newrect)
    screen.blit(ball.image, ball.rect)
    ball.move()

    pygame.draw.rect(screen, (255, 0, 0), surface1.rect, 1)
    pygame.draw.rect(screen, (0, 255, 0), newrect, 1)

    # 文字
    # font = pygame.font.SysFont("SimSun", 30)
    # text1 = font.render("SPACE: rotate circle", True, (255, 255, 255))
    # text2 = font.render("UP and DOWN: reverse gravity", True, (255, 255, 255))
    # screen.blit(text2, (10, 70))
    # screen.blit(text1, (10, 110))
    """ 显示FPS """
    text = "FPS: {0:.2f}".format(clock.get_fps())
    pygame.display.set_caption(text)

    """ 绘制所有surface对象 """
    pygame.display.flip()
