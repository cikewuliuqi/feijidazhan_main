"""Rect的作用"""
# import pygame

# hero_rect = pygame.Rect(100, 500, 120, 125)

# print("英雄的原点%d %d" % (hero_rect.x, hero_rect.y))
# print("英雄的尺寸%d %d" % (hero_rect.width, hero_rect.height))
"""创建游戏的主窗口"""
# pygame.display模块 用于创建管理游戏窗口
# 方法 .set_mode()初始化游戏显示窗口
# .update()刷新屏幕显示内容
# 了解一个模块需要知道四个方面 作用 参数 返回值 注意

# import pygame
# pygame.init()

# screen = pygame.display.set_mode((480, 700))
# while True:
#     pass
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()

# pygame.quit()
"""理解图像并实现图像绘制"""
# 1.使用pygame.image.load()加载图片的数据
# 2.使用游戏屏幕对象。调用blit方法绘制到指定的位置
# 3.调用pygame.display.update()方法更新整个屏幕的显示
# import pygame
# pygame.init()

# screen = pygame.display.set_mode((480, 700))
# while True:
#     bg = pygame.image.load("./feiji/background.png")
#     screen.blit(bg, (0, 0))
#     pygame.display.update()
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()

# pygame.quit()
"""绘制英雄图像以及透明图像的概念"""
# 1.知晓背景图片以及飞机图片的大小
# 2.位置的摆放，加减法容易(480,700)(100,124)
# 3.240-50=190  700 - 130 =570
# import pygame
# pygame.init()

# screen = pygame.display.set_mode((480, 700))
# while True:
#     bg = pygame.image.load("./feiji/background.png")
#     hero = pygame.image.load("./feiji/hero1.png")
#     screen.blit(bg, (0, 0))
#     screen.blit(hero, (190, 570))
#     pygame.display.update()
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()

# pygame.quit()
# png格式的图像支持透明的
# 在绘制图像时，透明区域不会显示任何内容
# 但是下方有内容，会透过透明区域显示出来
# """理解update()方法的作用"""
# 可以在screen对象的所有blit方法之后，统一调用一次dislay.update方法
# """3.1游戏中的动画实现原理"""
# 跟电影的原理类似。本质上是快速的在屏幕上绘制图像
# 一般电脑上每秒绘制60次。就能达到非常连续高质量的动画效果
# 每次绘制的结果被称为帧Frame
# pygame中每次调用update方法的结果就是一帧
# """3.2游戏循环"""
# 游戏的初始化：设置游戏窗口 绘制图像初始位置 设置游戏时钟
# 游戏循环  意味着游戏的正式开始 产生游戏效果
#         ：设置刷新帧率 检测用户交互 跟新所有图像位置 跟新屏幕显示
"""3.3英雄的简单动画实现"""

# import pygame
# pygame.init()
# screen = pygame.display.set_mode((480, 700))
# clock = pygame.time.Clock()
# i = 1
# while True:
#     clock.tick(0.5)
#     print(i)
#     i += 1
#     pass

# pygame.quit()
# 不需要执行的那么快
# pygame.time.Clock可以非常方便的设置屏幕绘制速度--刷新帧率
# 步骤需要两步 在程序初始化创建一个时钟对象  在游戏循环中让时钟
# 对象调用tick(帧率)的方法
# 可以指定循环体内部的代码执行的频率

"""3.4英雄的简单动画实现"""
# 需求1.在游戏初始化 定义一个pygame.Rect的变量记录英雄的初始位置
# 2.循环中让英雄每次y--向上移动
# 3.y<=0 时候英雄移动到屏幕的底部
# import pygame
# pygame.init()
# screen = pygame.display.set_mode((480, 700))
# clock = pygame.time.Clock()
# bg = pygame.image.load("./feiji/background.png")
# hero = pygame.image.load("./feiji/hero1.png")

# # 定义rect记录飞机的初始位置
# hero_rect = pygame.Rect(190, 570, 100, 124)
# while True:
#     clock.tick(60)
#     hero_rect.y -= 1
#     screen.blit(bg, (0, 0))
#     screen.blit(hero, hero_rect)
#     pygame.display.update()

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()


# pygame.quit()
# 图片的加载在循环之前，调用blit方法时候需要先加背景进行覆盖
# 不然就会有重影，最后update（）
# 提示：在每一次调用update之前，需要把所有的游戏图像都重新会
# 绘制一边
# 而且应该最先重新绘制背景图像
"""3.4英雄的简单动画实现 补充"""
# import pygame
# pygame.init()
# screen = pygame.display.set_mode((480, 700))
# clock = pygame.time.Clock()
# bg = pygame.image.load("./feiji/background.png")
# hero = pygame.image.load("./feiji/hero1.png")

# # 定义rect记录飞机的初始位置
# hero_rect = pygame.Rect(190, 570, 100, 124)
# while True:
#     clock.tick(60)
#     hero_rect.y -= 5
#     if hero_rect.y < -124:
#         hero_rect.y = 570
#     screen.blit(bg, (0, 0))
#     screen.blit(hero, hero_rect)
#     pygame.display.update()

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()


# pygame.quit()
"""3.5在游戏循环中的 监听 事件"""
# 事件 event
# .就是游戏启动后，用户针对游戏所做的操作
# 。例如：点击关闭按钮 点击鼠标 按下按键

# 监听
# 在游戏循环中，判断用户具体操作  例如：点击关闭按钮。点击按钮
# 按下按键

# 代码实现
# 。通过pygame.event.get()可以获得用户当前所做动作的事件列表
# 用户可以同一时间做很多事
# 提示：这段代码非常固定，几乎所有的pygame游戏都大同小异
# import pygame
# pygame.init()
# screen = pygame.display.set_mode((480, 700))
# clock = pygame.time.Clock()
# bg = pygame.image.load("./feiji/background.png")
# hero = pygame.image.load("./feiji/hero1.png")

# # 定义rect记录飞机的初始位置
# hero_rect = pygame.Rect(190, 570, 100, 124)
# while True:
#     clock.tick(60)
#     hero_rect.y -= 1
#     if hero_rect.y < -124:
#         hero_rect.y = 570
#     screen.blit(bg, (0, 0))
#     screen.blit(hero, hero_rect)
#     pygame.display.update()

#     for event in pygame.event.get():
#         #判断事件类型是否是退出事件
#         if event.type == pygame.QUIT:
#             pygame.quit()#卸载所有的模块
#             exit()#退出游戏循环


# pygame.quit()
"""04 理解精灵 和精灵组"""

"""4.1精灵和精灵组"""
# 。在刚刚完成的案件中，图像加载。位置变化，绘制图像 都需要
# 程序员编写代码分别处理
# 。为了简化来发步骤，pygame提供了两个类
# pygame.sprite.Sprite--存储图像数据image和位置rect的对象
# 。pygame.sprite.Group
# 精灵需要派生子类：image记录图像数据  rect记录在屏幕上的位置
# update(*args):更新精灵的位置  kill()从所有组中删除
# 精灵组 __init__(self,*jingling):
# add(*sprites):向组中增加精灵
# sprites():返回所有的精灵列表


# 在游戏的中
# 游戏初始化    1.创建精灵  2.创建精灵组
# 游戏循环      1.精灵组.update() 2.精灵组.draw(screee)
#          3.pygame.display.update()
"""4.2派生精灵子类"""
# import pygame

# class GameSprite(pygame.sprite.Sprite):
#     """
#         飞机大战游戏精灵
#     """

#     def __init__(self, image_name, speed=1):

#         #调用父类的初始化方法
#         super().__init__()

#         #定义对象属性
#         self.image = pygame.image.load(image_name)
#         self.rect = self.image.get_rect()
#         self.speed = speed

#     def update(self):

#         #在屏幕垂直方向上移动
#         self.rect.y += self.speed
"""4.3使用游戏精灵和精灵组创建敌机"""


# import pygame
# from plane_sprites import *
# pygame.init()

# screen = pygame.display.set_mode((480, 700))


# bg = pygame.image.load("./feiji/background.png")
# hero = pygame.image.load("./feiji/hero1.png")
# # 创建时钟对象
# clock = pygame.time.Clock()
# # 定义rect记录飞机的初始位置
# hero_rect = pygame.Rect(190, 570, 100, 124)

# # 创建敌机的精灵
# enemy = GameSprite("./feiji/enemy-1.gif")
# enemy1 = GameSprite("./feiji/enemy-1.gif", 2)
# # 创建敌机的精灵组
# enemy_group = pygame.sprite.Group(enemy, enemy1)

# while True:
#     clock.tick(60)
#     hero_rect.y -= 1
#     if hero_rect.y < -124:
#         hero_rect.y = 570

#     screen.blit(bg, (0, 0))
#     screen.blit(hero, hero_rect)

#     # 让精灵组调用两个方法
#     enemy_group.update()  # 让组中的所有精灵更新位置
#     enemy_group.draw(screen)  # 在screen上绘制所有的精灵

#     #
#     pygame.display.update()

#     for event in pygame.event.get():
#         # 判断事件类型是否是退出事件
#         if event.type == pygame.QUIT:
#             pygame.quit()  # 卸载所有的模块
#             exit()  # 退出游戏循环


# pygame.quit()
# """游戏框架搭建"""
# 一个游戏主程序的职责可以分为两个部分：
# 游戏初始化 游戏循环
"""2.3利用初始化方法，简化背景精灵创建"""

# 根据面向对象设计原则，应该将对象的职责，封装到类的代码内部
# 尽量简化程序调用一方的代码调用
"""2敌机出场"""
# 使用定时器添加敌机
# 设计enemy 类
# 敌机出现规律：每隔一秒出现一架飞机 没架敌机向屏幕下方飞行，飞行速度各不相同 每架飞机出现的水平
# 位置也不相同 当敌机行屏幕下方飞出，不会再飞回屏幕
# 1.1定时器
# 每隔一段时间，去执行一些动作pygame.time.set_time()
# 之后用监听的方法捕获事件列表
"""定义并监听创建敌机的定时器事件"""
# pygame 的定时器使用套路非常固定：
# 1.定义定时器常量--eventid
# 2.初始化方法中，调用set_timer方法设置定时器事件
# 3.在游戏循环中 ，监听定时器事件
# 初始化方法:指定敌机图片
# 随机敌机的初始位置和初始速度
"""随机敌机位置和速度"""
# 1）导入模块
# 顺序 1.官方标准模块导入 2.第三方模块导入 3.应用程序模块导入
"""移出屏幕销毁敌机"""
# 目的zaiyu 避免内存浪费
# __del__(self)zaikaifa中 用于判断对象是否被销毁

"""设计英雄和子弹类"""
# 从需求到设计
"""移动英雄位置"""
# 在pygame中针对键盘按键的捕获有两种方式
# 1.第一种方式event.type == pagame.KEYDOWN  必须手指抬起才能算作一次按键事件
# 2，pygame.key_get_pressed()  用户可以按住方向键不放，就可以持续向某个方向移动，操作性更好

"""碰撞检测"""
# pygame.sprite.pygame.sprite.pygame.sprite.groupcollide(
#     group1, group2, dokill1, dokill2, collided=None)
#     两个精灵组中的所有精灵的碰撞检测
# 判断某个精灵 和指定精灵组的 精灵的碰撞
# pygame.sprite.spritecollide(sprite, group, dokill, collided = None)
