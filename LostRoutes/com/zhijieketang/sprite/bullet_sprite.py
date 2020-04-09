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
# 代码文件：chapter26/LostRoutes/com/zhijieketang/sprite/bullet_sprite.py

import cocos.sprite


class Bullet(cocos.sprite.Sprite):
    def __init__(self):
        super(Bullet, self).__init__(image='resources/image/gameplay/bullet.png')
        # 子弹速度
        self.velocity = 360

    def shoot_bullet(self, node):
        """发射子弹"""

        # 获得精灵节点的位置
        x, y = node.position
        # 设置发送子弹的位置
        self.position = x, y + node.height // 2
        self.visible = True
        self.schedule(self.update)

    def update(self, dt):
        """游戏调度方法"""

        # 停止移除不可见的精灵节点
        if not self.visible:
            self.unschedule(self.update)
            return

        # 获得窗口的宽度和高度
        s_width, s_height = cocos.director.director.get_window_size()

        # 获得子弹位置
        posx, posy = self.position
        posy += self.velocity * dt
        # 设置子弹新位置
        self.position = posx, posy

        # 判断子弹是否飞出窗口
        if posy > s_height:
            self.visible = False
            self.unschedule(self.update)
