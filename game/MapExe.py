from game import MapUtils
from labyrinth import PrimLaby
import numpy as np
import pygame
from pygame.locals import *
from sys import exit

maze = PrimLaby.PrimMaze().getmaze()
print(maze)
map = MapUtils.Map(maze)

pygame.init()  # 初始化pygame
screen = pygame.display.set_mode((map.mazesize[0] * 50, map.mazesize[1] * 50))  # 显示窗口
wall = pygame.image.load('../PNG/wall.png')
# 创建seeker
player = pygame.image.load('../PNG/seeker.png')  # 加载图片
p_rect = player.get_rect()  # 获取矩形区域
speed = (0, 0)
reward = 0

while True:  # 死循环确保窗口一直显示
    for event in pygame.event.get():  # 遍历所有事件
        if event.type == pygame.QUIT:  # 如果单击关闭窗口，则退出
            exit()
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                speed = (1, 0)
            if event.key == K_LEFT:
                speed = (-1, 0)
            if event.key == K_UP:
                speed = (0, -1)
            if event.key == K_DOWN:
                speed = (0, 1)

            speed = map.state_move(speed)
            p_rect = p_rect.move([speed[0] * 50, speed[1] * 50])

    screen.fill((255, 255, 255))  # 填充颜色(设置为0，执不执行这行代码都一样)

    for i in map.walls:
        screen.blit(wall, (i[0] * 50, i[1] * 50))
    screen.blit(player, p_rect)  # 将图片画到窗口上
    pygame.display.flip()  # 更新全部显示