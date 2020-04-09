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
# 代码文件：chapter26/LostRoutes/com/zhijieketang/scene/setting_scene.py

"""设置场景"""
import configparser
import logging

import cocos
import cocos.layer
import cocos.scene
import cocos.scenes
import cocos.sprite
import pyglet

from com.zhijieketang.utility import tools

# 资源图片路径
from com.zhijieketang.utility.tools import add_to_scene

RES_PATH = 'resources/image/setting/'
logger = logging.getLogger(__name__)


class FuncBtn(object):
    def __init__(self, log_field, status=None, ctl=None):
        self.status = status
        self.ctl = ctl
        self.log_field = log_field

class SettingLayer(cocos.layer.Layer):
    is_event_handler = True

    def __init__(self):
        super(SettingLayer, self).__init__()

        logger.info('初始化设置层')

        add_to_scene(self, RES_PATH + 'bg.png')

        # # 读取配置信息
        self.config = configparser.ConfigParser()
        self.config.read('config.ini', encoding='utf-8')
        # 读取音效状态
        self.sound = FuncBtn('sound_status')
        self.music = FuncBtn('music_status')

        self.sound.status = self.config.getint('setting', 'sound_status')
        # 读取背景音乐状态
        self.music.status = self.config.getint('setting', 'music_status')

        self.check_on_image = pyglet.resource.image(RES_PATH + 'check-on.png')
        self.check_off_image = pyglet.resource.image(RES_PATH + 'check-off.png')

        self.sound.ctl = self.make_check_button(self.sound.status, 210, 328)
        self.music.ctl = self.make_check_button(self.music.status, 210, 270)

    def make_check_button(self, status, x, y):
        ctl = self.load_img(status)
        ctl.position = x, y
        self.add(ctl, 0)
        return ctl

    def load_img(self, status):
        # 读取配置信息
        if status == 0:
            img = cocos.sprite.Sprite(self.check_off_image)
        else:
            img = cocos.sprite.Sprite(self.check_on_image)
        return img

    def on_mouse_release(self, x, y, button, modifiers):
        if button == pyglet.window.mouse.LEFT:
            # 音效复选框精灵矩形轮廓
            soundchkrect = self.sound.ctl.get_rect()
            # 背景音乐复选框精灵矩形轮廓
            musicchkrect = self.music.ctl.get_rect()

            # 单击音效复选框精灵
            if soundchkrect.contains(x, y):
                logger.debug('单击音效复选框精灵')
                self.handle_click(self.sound)

            # 单击背景音乐复选框精灵
            if musicchkrect.contains(x, y):
                logger.debug('单击音乐复选框精灵')
                self.handle_click(self.music)

    def handle_click(self, btn):
        if btn.status == 0:
            # 音效开启
            btn.ctl.image = self.check_on_image
            btn.status = 1
        else:
            # 音效未开启
            btn.ctl.image = self.check_off_image
            btn.status = 0
        # 写入音效状态
        self.config['setting'][btn.log_field] = str(btn.status)
        with open('config.ini', 'w') as fw:
            self.config.write(fw)


class MainMenu(cocos.menu.Menu):

    def __init__(self):
        super(MainMenu, self).__init__()

        logger.info('初始化MainMenu')

        # 菜单项初始化设置
        self.font_item['font_size'] = 60
        self.font_item['color'] = (180, 200, 255, 255)
        self.font_item_selected['color'] = (255, 255, 255, 255)
        self.font_item_selected['font_size'] = 60

        ok_item = cocos.menu.ImageMenuItem(RES_PATH + 'button-ok.png',
                                              self.on_item_callback)

        self.create_menu([ok_item],
                         layout_strategy=cocos.menu.fixedPositionMenuLayout(
                             [(210, 50)]))

    def on_item_callback(self):
        cocos.director.director.pop()
        # 播放音效
        tools.playeffect('Blip.wav')


def create_scene():
    """创建设置场景函数"""

    # 创建设置场景
    scene = cocos.scene.Scene(SettingLayer())
    # 添加主菜单
    scene.add(MainMenu())

    return scene
