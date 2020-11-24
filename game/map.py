import pygame
from pygame.locals import *
from sys import exit
import numpy as np


maze = np.array([[255, 255, 255, 255, 255, 255, 255, 0, 255],
                 [0, 0, 255, 0, 255, 0, 0, 0, 255],
                 [255, 0, 255, 0, 255, 255, 255, 0, 255],
                 [255, 0, 255, 0, 255, 0, 255, 0, 255],
                 [255, 255, 255, 0, 255, 0, 255, 255, 255],
                 [0, 0, 255, 0, 0, 0, 0, 0, 255],
                 [255, 255, 255, 255, 255, 255, 255, 0, 255],
                 [255, 0, 255, 0, 0, 0, 255, 0, 255],
                 [255, 0, 255, 255, 255, 0, 255, 0, 255]],)

pygame.init()  # 初始化pygame
size = width, height = 450, 450  # 设置窗口大小
screen = pygame.display.set_mode(size)  # 显示窗口
color = (255, 255, 255)  # 设置颜色
ball = pygame.image.load('PNG/seeker.png')  # 加载图片
wall = pygame.image.load('PNG/wall.png')
wall_pos = []
wall_list = []
for i in range(9):
    for j in range(9):
        if maze[i, j] == 0:
            temp = i, j
            wall_pos.append(temp)
            temp = pygame.image.load('PNG/wall.png'), (i * 50, j * 50)
            wall_list.append(temp)

print(wall_list)
background = pygame.image.load('PNG/PRIM1.png')
ballrect = ball.get_rect()  # 获取矩形区域

speed = [50, 50]  # 设置移动的X轴、Y轴

while True:  # 死循环确保窗口一直显示
    for event in pygame.event.get():  # 遍历所有事件
        if event.type == pygame.QUIT:  # 如果单击关闭窗口，则退出
            exit()
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                ballrect = ballrect.move([50,0])
            if event.key == K_LEFT:
                ballrect = ballrect.move([-50, 0])
            if event.key == K_UP:
                ballrect = ballrect.move([0, -50])
            if event.key == K_DOWN:
                ballrect = ballrect.move([0, 50])

    # # 碰到左右边缘
    # if ballrect.left < 0 or ballrect.right > width:
    #     speed[0] = -speed[0]
    # # 碰到上下边缘
    # if ballrect.top < 0 or ballrect.bottom > height:
    #     speed[1] = -speed[1]

    screen.fill(color)  # 填充颜色(设置为0，执不执行这行代码都一样)
    for i in wall_list:
        print(i)
        screen.blit(i[0], i[1])
    screen.blit(ball, ballrect)  # 将图片画到窗口上
    pygame.display.flip()  # 更新全部显示

pygame.quit()  # 退出pygame

