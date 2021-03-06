# coding=utf-8
# Created by 智捷关东升
# 本书网站：www.zhijieketang.com/group/8
# 智捷课堂在线课堂：www.zhijieketang.com
# 智捷课堂微信公共号：zhijieketang
# 邮箱：eorient@sina.com
# 读者服务QQ群：628808216
# 【配套电子书】网址：
#       百度阅读：
#       https://yuedu.baidu.com/ebook/5823871e59fafab069dc5022aaea998fcc2240fc
# 代码文件：chapter26/LostRoutes/com/zhijieketang/scene/gameover_scene.py


import dbm
import logging
import os

import cocos
import cocos.layer
import cocos.scene
import cocos.scenes
import cocos.sprite

from com.zhijieketang.utility import tools

# 资源图片路径
from com.zhijieketang.utility.tools import add_to_scene

RES_PATH = 'resources/image/gameover/'
HIGHSCORE_KEY = 'high_score'
SCORE_KEY = 'score'
DB_NAME = 'db/game.db'

logger = logging.getLogger(__name__)


# 自定义GameOverLayer层类
class GameOverLayer(cocos.layer.Layer):
    is_event_handler = True

    def __init__(self, score):
        super(GameOverLayer, self).__init__()

        self.score = score

        # 获得窗口的宽度和高度
        s_width, s_height = cocos.director.director.get_window_size()

        # 创建db文件夹
        if not os.path.exists('db'):
            os.mkdir('db')

        with dbm.open(DB_NAME, 'c') as db:

            highscore = db.get(HIGHSCORE_KEY, b'0').decode()
            logger.info(highscore)

            if int(highscore) < self.score:
                highscore = str(self.score)
                db[HIGHSCORE_KEY] = highscore

        self.scorelabel = cocos.text.Label(highscore,
                                           font_name='Harlow Solid Italic',
                                           font_size=17,
                                           anchor_x='center', anchor_y='center')
        self.scorelabel.position = s_width // 2 + 30, 136
        self.add(self.scorelabel, 1)

        # 创建背景精灵
        add_to_scene(self, RES_PATH + 'bg.png')


class MainMenu(cocos.menu.Menu):

    def __init__(self):
        super(MainMenu, self).__init__()

        # 获得窗口的宽度和高度
        s_width, s_height = cocos.director.director.get_window_size()

        # 菜单项初始化设置
        self.font_item['font_name'] = 'Century Gothic'
        self.font_item['font_size'] = 17
        self.font_item['color'] = (255, 255, 255, 255)
        self.font_item_selected['font_name'] = 'Century Gothic'
        self.font_item_selected['color'] = (255, 255, 255, 255)
        self.font_item_selected['font_size'] = 17

        start_item = cocos.menu.MenuItem('Tap the Screen to Play', self.on_item_callback)

        self.create_menu([start_item],
                         layout_strategy=cocos.menu.fixedPositionMenuLayout(
                             [(s_width // 2, 70)]))

    def on_item_callback(self):
        cocos.director.director.pop()
        # 播放音效
        tools.playeffect('Blip.wav')


# 创建场景函数
def create_scene(score):
    # 创建场景
    scene = cocos.scene.Scene(GameOverLayer(score))
    # 添加主菜单
    scene.add(MainMenu())
    return scene
