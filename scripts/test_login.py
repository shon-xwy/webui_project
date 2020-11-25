'''
@Author:shon
'''
import unittest
from parameterized import parameterized
from page.page_login import PageLogin
from tool.operate_driver import OperateDriver
from tool import read_txt


class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        # 实例化登录模块对象，并出入driver对象
        cls.login = PageLogin(OperateDriver().get_driver())
        # 点击首页登录按钮
        cls.login.page_click_index_login_btn()


    @classmethod
    def tearDownClass(cls) -> None:
        OperateDriver().close_driver()

    # def test_login_001(self):
    #     self.login.page_click_index_login_btn()
    #     self.login.page_input_username('ycy666')
    #     self.login.pase_click_login_btn()
    #     pwd_tips = self.login.page_pwd_null_tips()
    #     print(pwd_tips)
    #     self.assertEqual(pwd_tips,'密码不能为空')

    @parameterized.expand(read_txt.read_txt('login_data.txt'))
    def test_login_002(self,username,password,stats):
        self.login.page_input_username(username)
        self.login.pase_input_password(password)
        self.login.pase_click_login_btn()
        if stats == 'true':
            ele = self.login.page_quit_login_btn_exist()
            self.assertTrue(ele)
        else:
            pwd_tips = self.login.page_pwd_null_tips()
            self.assertEqual(pwd_tips, '密码不能为空')