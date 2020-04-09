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
# 代码文件：chapter26/LostRoutes/com/zhijieketang/utility/tools.py

import configparser

import cocos
from cocos.audio.effect import Effect
from cocos.audio.pygame import music

# 读取配置信息
config = configparser.ConfigParser()
# 声音资源路径
RES_PATH = 'resources/sound/'


def playmusic(soundfile, musicstatus=None):
    """播放背景音乐"""

    if musicstatus is None:
        config.read('config.ini', encoding='utf-8')
        # 读取背景音乐状态
        musicstatus = config.getint('setting', 'music_status')

    if musicstatus == 1:
        # 播放背景音乐
        music.load((RES_PATH + soundfile).encode())  # 加载背景音乐
        if music.get_busy():
            return
        music.play(loops=-1)  # 循环播放背景音乐
        music.set_volume(0.2)  # 设置音量最大
    else:
        music.stop()


def playeffect(soundfile):
    """播放音效"""

    config.read('config.ini', encoding='utf-8')
    # 读取音效状态
    soundstatus = config.getint('setting', 'sound_status')
    if soundstatus == 1:
        effect = Effect(RES_PATH + soundfile)
        effect.play()

def add_to_scene(self, path, point = (-1, -1)):
    # 创建背景精灵
    spirit = cocos.sprite.Sprite(path)
    if point == (-1, -1):
        point = cocos.director.director.get_window_size()

    spirit.position = point[0] // 2, point[1] // 2
    self.add(spirit, 0)

def show_next_scene(next_scene):
    ts = cocos.scenes.FadeTransition(next_scene, 1.0)
    cocos.director.director.push(ts)
    playeffect('Blip.wav')