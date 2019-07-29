import pygame
from plane_sprites import *


class PlaneGame(object):
    """飞机大战主游戏"""

    def __init__(self):
        print("游戏初始化")

        # 1.创建游戏的窗口
        self.screen = pygame.display.set_mode((SCREEN_RECT.size))
        # 2.创建游戏的时钟
        self.clock = pygame.time.Clock()
        # 3.调用私有方法，精灵和精灵组的创建
        self.__create_sprites()

        # 4.设置定时器事件-创建敌机 1s
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)
        pygame.time.set_timer(HERO_FIRE_EVENT, 500)
        pygame.time.set_timer(CREATE_BIGENEMY_EVENT, 3000)

    def __create_sprites(self):

        # 创建背景精灵和精灵组
        bg1 = Background()
        bg2 = Background(True)
        self.back_group = pygame.sprite.Group(bg1, bg2)

        # 创建敌机的精灵组
        self.enemy_group = pygame.sprite.Group()

        # 创建英雄精灵和精灵组
        self.hero = Hero()  # 把英雄定义为属性，因为后面需要英雄调用发射子弹和碰撞检测
        self.hero_group = pygame.sprite.Group(self.hero)

        # 创建大飞机精灵和精灵组
        # self.big_enemy = Big_Enemy()
        self.big_enemy_group = pygame.sprite.Group()

    def start_game(self):
        print("游戏开始")

        while True:
            # 设置刷新帧率
            self.clock.tick(FRAME_PER_SEC)
            # 事件监听
            self.__event_handler()
            # 碰撞检测
            self.__check_collide()
            # 更新绘制精灵组
            self.__update_sprite()
            # 更新屏幕显示
            pygame.display.update()

    def __event_handler(self):

        for event in pygame.event.get():

            # 判断是否退出游戏
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()

            elif event.type == CREATE_ENEMY_EVENT:
               # print("敌机出场...")
                # 创建敌机精灵
                enemy = Enemy()
                # 将敌机精灵添加到敌机精灵组
                self.enemy_group.add(enemy)
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()
            # elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            #     print("向右移动...")
        # 使用键盘提供的方法获取按键
            elif event.type == CREATE_BIGENEMY_EVENT:
                print("大boss出现")
                big_enemy = Big_Enemy()
                # 将敌机精灵添加到敌机精灵组
                self.big_enemy_group.add(big_enemy)
        keys_pressed = pygame.key.get_pressed()
        # 判断元祖中对应的按键索引值 1
        if keys_pressed[pygame.K_a]:
            self.hero.speed = -3
        elif keys_pressed[pygame.K_d]:
            self.hero.speed = +3
        elif keys_pressed[pygame.K_w]:
            self.hero.rect.y -= 3
            # if self.hero.rect.y > "574"
            # self.hero.rect.y = "574"
            # 为什么这样不行
        elif keys_pressed[pygame.K_s]:
            self.hero.rect.y += 3

        else:
            self.hero.speed = 0
        # 加上elst之后完整才能实现松开即停

    def __check_collide(self):
        # 1.子弹摧毁敌机
        pygame.sprite.pygame.sprite.groupcollide(
            self.hero.bullets, self.enemy_group, True, True, )

        # 2.敌机撞毁英雄
        enemies = pygame.sprite.pygame.sprite.spritecollide(
            self.hero, self.enemy_group, True)
        # 3.子弹摧毁打飞机
        pygame.sprite.pygame.sprite.groupcollide(
            self.hero.bullets, self.big_enemy_group, True, True, )

        # 判断列表是否有内容
        if len(enemies) > 0:
            self.hero.kill()
            PlaneGame.__game_over()

    def __update_sprite(self):
        self.back_group.update()
        self.back_group.draw(self.screen)
        self.enemy_group.update()
        self.enemy_group.draw(self.screen)
        self.hero_group.update()
        self.hero_group.draw(self.screen)
        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)
        self.big_enemy_group.update()
        self.big_enemy_group.draw(self.screen)

    @staticmethod
    def __game_over():
        print("游戏结束")

        pygame.quit()
        exit()


if __name__ == "__main__":

    # 创建游戏对象
    game = PlaneGame()

    # 启动游戏
    game.start_game()
