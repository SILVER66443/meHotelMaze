from game import map_utils
from labyrinth import prim_self
import numpy as np
import pygame
from pygame.locals import *
from sys import exit

maze = prim_self.prim_Maze().getMaze()
map = map_utils.Map(maze)

pygame.init()  # 初始化pygame
screen = pygame.display.set_mode((map.size[0] * 50, map.size[1] * 50))  # 显示窗口
wall = pygame.image.load('../PNG/wall.png')
# 创建seeker
player = pygame.image.load('../PNG/seeker.png')  # 加载图片
p_rect = player.get_rect()  # 获取矩形区域

while True:  # 死循环确保窗口一直显示
    for event in pygame.event.get():  # 遍历所有事件
        if event.type == pygame.QUIT:  # 如果单击关闭窗口，则退出
            exit()
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                map.set_step([1, 0])
            if event.key == K_LEFT:
                map.set_step([-1, 0])
            if event.key == K_UP:
                map.set_step([0, -1])
            if event.key == K_DOWN:
                map.set_step([0, 1])

            step = map.move()
            p_rect = p_rect.move([step[0]*50,step[1]*50])

    screen.fill((255, 255, 255))  # 填充颜色(设置为0，执不执行这行代码都一样)

    for i in map.wall_list:
        screen.blit(wall, (i[0] * 50, i[1] * 50))
    screen.blit(player, p_rect)  # 将图片画到窗口上
    pygame.display.flip()  # 更新全部显示

pygame.quit()
