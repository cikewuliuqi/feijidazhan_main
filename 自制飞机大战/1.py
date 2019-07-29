import pygame
import time
from pygame.locals import *


def main():
    # 1.创建窗口
    screen = pygame.display.set_mode((480, 852), 0, 32)

    # 2.创建一个背景图片
    backgroup = pygame.image.load('./feiji/background.png')

    # 3.创建一个飞机图片
    hero = pygame.image.load('./feiji/hero1.png')
    x = 210
    y = 700

    while True:

        screen.blit(backgroup, (0, 0))

        screen.blit(hero, (x, y))
        pygame.display.update()
        time.sleep(0.01)

        for event in pygame.event.get():
            if event.type == QUIT:
                print("exit")
                exit()
            elif event.type == KEYDOWN:
                if event.key == K_a or event.key == K_LEFT:
                    print('left')
                    x -= 5
                elif event.key == K_d or event.key == K_RIGHT:
                    print('right')
                    x += 5

                elif event.key == K_SPACE:
                    print('space')


if __name__ == "__main__":
    main()
