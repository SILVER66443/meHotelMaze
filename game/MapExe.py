from game import GameUtils
from labyrinth import PrimLaby
import numpy as np
import pygame
from pygame.locals import *
from sys import exit

# constant declaration
BOARDWIDTH = 1280  # width
BOARDHEIGHT = 768  # height
UNITSIZE = 30  # square size
MAZE_SIZE = (19,19)  # mazement size
assert MAZE_SIZE[0] % 2 != 0 and MAZE_SIZE[1] % 2 != 0, "The size parameter of mazement shoud be set to an even number!"
POS_BIAS = (int((BOARDWIDTH - MAZE_SIZE[0] * UNITSIZE) / 2), int((BOARDHEIGHT - MAZE_SIZE[1] * UNITSIZE) / 2))

# Color declaration
#        R    G    B
GRAY = (100, 100, 100)
NAVYBLUE = (60, 60, 100)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 128, 0)
PURPLE = (255, 0, 255)
CYAN = (0, 255, 255)


def main():
    # get maze
    maze = PrimLaby.PrimMaze(MAZE_SIZE).getmaze()
    map = GameUtils.Map(maze)

    pygame.init()  # 初始化pygame
    screen = pygame.display.set_mode((BOARDWIDTH, BOARDHEIGHT))  # 显示窗口
    wall = pygame.image.load('../PNG/wall.png')
    wall = pygame.transform.scale(wall, (30, 30))

    # 创建seeker
    player = pygame.image.load('../PNG/seeker.png')  # 加载图片
    player = pygame.transform.scale(player, (30, 30))
    p_rect = player.get_rect()  # 获取矩形区域
    p_rect.left = POS_BIAS[0]
    p_rect.top = POS_BIAS[1]

    speed = (0, 0)
    screen.fill(NAVYBLUE)
    while True:  # 死循环确保窗口一直显示
        screen.fill(NAVYBLUE)
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
                p_rect = p_rect.move([speed[0] * 30, speed[1] * 30])

        # for i in map.walls:
        #     screen.blit(wall, (i[0] * 30, i[1] * 30))
        for i in range(MAZE_SIZE[0]):
            for j in range(MAZE_SIZE[1]):
                if (i, j) in map.walls:
                    # screen.blit(wall, [i * 30 + POS_BIAS[0], j * 30 + POS_BIAS[1]])
                    pygame.draw.rect(screen, NAVYBLUE, (i * 30 + POS_BIAS[0], j * 30 + POS_BIAS[1], 30, 30))
                else:
                    pygame.draw.rect(screen, CYAN, (i * 30 + POS_BIAS[0], j * 30 + POS_BIAS[1], 30, 30))

        screen.blit(player, p_rect)  # 将图片画到窗口上
        pygame.display.update()  # 更新全部显示


if __name__ == '__main__':
    main()
