# 面向对象的思想将1.py进行改写
import pygame
import time
from pygame.locals import *
import random


class HeroPlane():
    def __init__(self, screen_temp):
        self.x = 210
        self.y = 700
        self.screen = screen_temp
        self.image = pygame.image.load('./feiji/hero1.png')
        self.bullet_list = []  # 存储发射出去的子弹对象引用

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()
            if bullet.judge():  # 判断子弹是否越界
                self.bullet_list.remove(bullet)

    def move_right(self):
        self.x += 10

    def move_left(self):
        self.x -= 10

    def move_up(self):
        self.y -= 10

    def move_down(self):
        self.y += 10

    def fire(self):
        self.bullet_list.append(Bullet(self.screen, self.x, self.y))


class EnemyPlane():
    def __init__(self, screen_temp):
        self.x = 0
        self.y = 0
        self.screen = screen_temp
        self.image = pygame.image.load('./feiji/enemy-1.gif')
        self.bullet_list = []  # 存储发射出去的子弹对象引用
        self.direction = "right"  # 用来存储飞机默认的显示方向

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()
        if bullet.judge():  # 判断子弹是否越界
            self.bullet_list.remove(bullet)

    def move(self):
        if self.direction == "right":
            self.x += 5
        elif self.direction == "left":
            self.x -= 5
        if self.x > 480-50:
            self.direction = "left"
        if self.x < 0:
            self.direction = "right"

    def fire(self):
        if random.randint(1, 100) == 7:
            self.bullet_list.append(EnemyBullet(self.screen, self.x, self.y))


class Bullet():
    def __init__(self, screen_temp, x, y):
        self.x = x + 40
        self.y = y - 20
        self.screen = screen_temp
        self.image = pygame.image.load('./feiji/bullet-3.gif')

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    def move(self):
        self.y -= 5

    def judge(self):
        if self.y < 0:
            return True

        else:
            return False


class EnemyBullet():
    def __init__(self, screen_temp, x, y):
        self.x = x+25
        self.y = y+40
        self.screen = screen_temp
        self.image = pygame.image.load('./feiji/bullet1.png')

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()
            if bullet.judge():  # 判断子弹是否越界
                self.bullet_list.remove(bullet)

    def move(self):
        self.y += 5

    def judge(self):
        if self.y > 500:
            return True

        else:
            return False


def key_control(hero_temp):
    # 获取事件，比如按键等
    for event in pygame.event.get():
        if event.type == QUIT:
            print("exit")
            exit()
        elif event.type == KEYDOWN:
            if event.key == K_a or event.key == K_LEFT:
                print('left')
                hero_temp.move_left()
            elif event.key == K_d or event.key == K_RIGHT:
                print('right')
                hero_temp.move_right()
            elif event.key == K_SPACE:
                print('space')
                hero_temp.fire()
            elif event.key == K_w or event.key == K_UP:
                hero_temp.move_up()
            elif event.key == K_s or event.key == K_DOWN:
                hero_temp.move_down()


def main():
    # 1.创建窗口
    screen = pygame.display.set_mode((480, 852), 0, 32)

    # 2.创建一个背景图片
    backgroup = pygame.image.load('./feiji/background.png')

    # 3.创建一个飞机图片
    hero = HeroPlane(screen)
    # 4.创建一个敌机图片
    enemy = EnemyPlane(screen)

    while True:

        screen.blit(backgroup, (0, 0))
        hero.display()
        enemy.display()
        enemy.move()
        enemy.fire()
        pygame.display.update()
        key_control(hero)
        time.sleep(0.01)


if __name__ == "__main__":
    main()
