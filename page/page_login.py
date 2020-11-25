'''
@Author:shon
'''
from base.base import Base
import page

class PageLogin(Base):

    # 点击首页的登录按钮
    def page_click_index_login_btn(self):
        self.base_click(page.index_login_btn)

    # 输入用户名
    def page_input_username(self,username):
        self.base_input(page.username,username)

    # 输入密码
    def pase_input_password(self,password):
        self.base_input(page.password,password)

    # 点击登录按钮
    def pase_click_login_btn(self):
        self.base_click(page.login_btn)

    # 密码为空的提示信息--断言
    def page_pwd_null_tips(self):
        return self.base_get_texts(page.pwd_null_tips,1)

    # 登录成功后的退出按钮是否存在--断言
    def page_quit_login_btn_exist(self):
        return self.base_if_exist(page.quit_login_ok_btn)