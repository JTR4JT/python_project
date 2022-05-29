import unittest
import win32api
import win32con
from unittest.mock import Mock
from pymouse import PyMouse
from unittest import TestCase
from alien_invasion import AlienInvasion

class TestShipMovement(TestCase):
    """针对AlienInvasion类中方法的测试"""

    # def test_click_play_button(self):
    #     """测试点击Play按钮"""
    #     ai = AlienInvasion()
    #     mock_g = Mock(return_value=ai)
    #     mock_obj = mock_g()
    #
    #     # 验证游戏是否为非活动状态
    #     self.assertEqual(mock_obj.stats.game_active, False)
    #     # 点击Play按钮
    #     m = PyMouse()
    #     m.click(750, 500)
    #     # 更新游戏状态
    #     mock_obj._check_events()
    #     # 判断游戏是否为活动状态
    #     self.assertEqual(mock_obj.stats.game_active, True)


    def test_ship_moving_left(self):
        """测试飞船左移"""
        ai = AlienInvasion()
        mock_g = Mock(return_value=ai)
        mock_obj = mock_g()

        # 按左键
        win32api.keybd_event(37, 0, 0, 0)
        # 更新游戏状态
        for i in range(100):
            mock_obj._check_events()
            mock_obj.ship.update()
        # 判断按左键时moving_left是否为True
        self.assertEqual(mock_obj.ship.moving_left, True)
        # 判断飞船是否出界
        self.assertEqual(mock_obj.ship.rect.left >= 0, True)

        # 松开左键
        win32api.keybd_event(37, 0, win32con.KEYEVENTF_KEYUP, 0)
        mock_obj._check_events()
        mock_obj.ship.update()
        # 判断松开左键后moving_left是否变为False
        self.assertEqual(mock_obj.ship.moving_left, False)


    def test_ship_moving_right(self):
        """测试飞船右移"""
        ai = AlienInvasion()
        mock_g = Mock(return_value=ai)
        mock_obj = mock_g()

        # 按右键
        win32api.keybd_event(39, 0, 0, 0)
        # 更新游戏状态
        for i in range(100):
            mock_obj._check_events()
            mock_obj.ship.update()
        # 判断按右键时moving_right是否为True
        self.assertEqual(mock_obj.ship.moving_right, True)
        self.assertEqual(mock_obj.ship.rect.right <= mock_obj.screen.get_rect().right, True)

        # 松开右键
        win32api.keybd_event(39, 0, win32con.KEYEVENTF_KEYUP, 0)
        mock_obj._check_events()
        mock_obj.ship.update()
        # 判断松开右键后moving_right是否变为False
        self.assertEqual(mock_obj.ship.moving_right, False)


    def test_fire_bullet(self):
        """测试发射子弹"""
        ai = AlienInvasion()
        mock_g = Mock(return_value=ai)
        mock_obj = mock_g()

        i = 1
        while i == 10:
            break
        else :
            # 按空格键
            win32api.keybd_event(32, 0x39, 0, 0)
            # 更新游戏状态
            mock_obj._check_events()
            # 判断按下空格键后子弹是否产生
            self.assertEqual(len(mock_obj.bullets), i)
            i = i + 1



if __name__ == '__main__':
    unittest.main()
    
    


        



        