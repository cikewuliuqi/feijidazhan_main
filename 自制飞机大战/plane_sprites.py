import random
import pygame

# 屏幕大小的常量
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
# 刷新的帧率
FRAME_PER_SEC = 60
# 创建敌机的定时器常量
CREATE_ENEMY_EVENT = pygame.USEREVENT
# 创建英雄发射子弹事件
HERO_FIRE_EVENT = pygame.USEREVENT+1
# 创建大敌机的定时器常量
CREATE_BIGENEMY_EVENT = pygame.USEREVENT+2


class GameSprite(pygame.sprite.Sprite):
    """
        飞机大战游戏精灵
    """

    def __init__(self, image_name, speed=1):

        # 调用父类的初始化方法
        super().__init__()

        # 定义对象属性
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):

        # 在屏幕垂直方向上移动
        self.rect.y += self.speed


class Background(GameSprite):
    """游戏背景精灵"""

    def __init__(self, is_alt=False):

        # 1.调用父类方法实现精灵类的创建()
        super().__init__("./feiji/background.png")
        # 2.判断是否是交替图像，如果是，需要设置厨师位置
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):
        # 1.调用父类的方法实现
        super().update()

        # 2.判断是否移出屏幕，如果移出屏幕 将图像设置到屏幕的上方
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height


class Enemy(GameSprite):

    """敌机精灵"""

    def __init__(self):
        # 1.调用父类方法。创建敌机精灵，同时指定敌机图片
        super().__init__("./feiji/enemy1.png")
        # 2.指定敌机的初始随机速度
        self.speed = random.randint(1, 3)
        # 3.指定敌机的初始随机位置
        self.rect.bottom = 0

        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)

    def update(self):
        # 1.调用父类方法。保持垂直方向的飞行
        super().update()
        # 2，判断是否飞出屏幕，如果是。需要从精灵组删除敌机
        if self.rect.y >= SCREEN_RECT.height:
            # print("飞出屏幕。需要性精灵组中删除...")
            # kill方法可可以讲所有精灵组中移出，精灵就会被自动销毁
            self.kill()

    def __del__(self):  # 判断敌机是否被销毁
        # print("敌机挂了%s" % self.rect)
        pass


class Hero(GameSprite):
    """英雄精灵"""

    def __init__(self):
        # 1.调用父类方法，设置image and speed
        super().__init__("./feiji/me1.png", 0)
        # 2.设置英雄的初始位置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120

        # 创建子弹的精灵组
        self.bullets = pygame.sprite.Group()

    def update(self):
        # 英雄在水平方向上移动
        self.rect.x += self.speed
        # 控制英雄不能离开屏幕
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right
        if self.rect.y > 574:
            self.rect.y = 574

    def fire(self):
        print("子弹发射")
        # 发射三发子弹
        # for i in (0, 1, 2):

        #     # 创建子弹精灵
        #     bullet = Bullet()
        #     # 设置子弹精灵的位置
        #     bullet.rect.bottom = self.rect.y-i*20
        #     bullet.rect.centerx = self.rect.centerx

        #     # 将精灵添加到精灵组
        #     self.bullets.add(bullet)
        # for i in (0, 1, 2):

        # 创建子弹精灵
        bullet = Bullet()
        # 设置子弹精灵的位置
        bullet.rect.bottom = self.rect.y-20
        bullet.rect.centerx = self.rect.centerx

        # 将精灵添加到精灵组
        self.bullets.add(bullet)


class Bullet(GameSprite):
    def __init__(self):
        super().__init__("./feiji/bullet-3.gif", -2)

    def update(self):
        super().update()
        if self.rect.bottom < 0:
            self.kill()

    def __del__(self):
        print("子弹被销毁")


class Big_Enemy(GameSprite):

    """大boss出现"""

    def __init__(self):
        # 1.调用父类方法。创建敌机精灵，同时指定敌机图片
        super().__init__("./feiji/enemy-2.gif")
        # 2.指定敌机的初始随机速度
        self.speed = random.randint(1, 3)
        # 3.指定敌机的初始随机位置
        self.rect.bottom = 0

        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)

    def update(self):
        # 1.调用父类方法。保持垂直方向的飞行
        super().update()
        # 2，判断是否飞出屏幕，如果是。需要从精灵组删除敌机
        if self.rect.y >= SCREEN_RECT.height:
            # print("飞出屏幕。需要性精灵组中删除...")
            # kill方法可可以讲所有精灵组中移出，精灵就会被自动销毁
            self.kill()

    def __del__(self):  # 判断敌机是否被销毁
        # print("敌机挂了%s" % self.rect)
        pass
