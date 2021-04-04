import pygame
from pygame.locals import *
import sys
import random


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("G:/pyProject/meHotelMaze/PNG/wall.png")
        self.rect = self.image.get_rect()
        self.rect.top = 100.5
        self.rect.left = 500
        self.speed = (2, 2)


def blitRotate(surf, image, pos, originPos, angle):
    # calculate the axis aligned bounding box of the rotated image
    w, h = image.get_size()
    box = [pygame.math.Vector2(p) for p in [(0, 0), (w, 0), (w, -h), (0, -h)]]
    box_rotate = [p.rotate(angle) for p in box]
    min_box = (min(box_rotate, key=lambda p: p[0])[0], min(box_rotate, key=lambda p: p[1])[1])
    max_box = (max(box_rotate, key=lambda p: p[0])[0], max(box_rotate, key=lambda p: p[1])[1])

    # calculate the translation of the pivot
    pivot = pygame.math.Vector2(originPos[0], -originPos[1])
    pivot_rotate = pivot.rotate(angle)
    pivot_move = pivot_rotate - pivot

    # calculate the upper left origin of the rotated image
    origin = (pos[0] - originPos[0] + min_box[0] - pivot_move[0], pos[1] - originPos[1] - max_box[1] + pivot_move[1])

    # get a rotated image
    rotated_image = pygame.transform.rotate(image, angle)

    # draw rectangle around the image
    pygame.draw.rect(surf, (255, 0, 0), (*origin, *rotated_image.get_size()), 2)

    # rotate and blit the image
    surf.blit(rotated_image, origin)


def main():
    pygame.init()
    running = True

    bg_size = 1024, 681
    screen = pygame.display.set_mode(bg_size)
    pygame.display.set_caption("Demo_Test")

    ball = Ball()
    w, h = ball.image.get_size()
    clock = pygame.time.Clock()
    angle = 0
    pos = (300, 300)
    screen.fill((60, 60, 100))
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
        image = pygame.transform.rotate(ball.image, angle)
        angle += 1

        blitRotate(screen, ball.image, pos, (w/3, h/3), angle)

        # screen.blit(ball.image, ball.rect)
        # screen.blit(image, (200, 200))
        pygame.display.flip()
        clock.tick(30)


if __name__ == "__main__":
    main()
