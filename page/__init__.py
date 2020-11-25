'''
@Author:shon
'''
from selenium.webdriver.common.by import By
''' 打开需要测试的地址 '''
URL = 'http://fshon.6868hy.com/'

''' 登录功能--元素信息'''
# 首页登录按钮
index_login_btn = By.CSS_SELECTOR,'[class="iconfont icon-user"]'
# 用户名
username = By.CSS_SELECTOR,'[placeholder="请输入账号"]'
# 密码
password = By.CSS_SELECTOR,'[placeholder="请输入密码"]'
# 登录按钮
login_btn = By.CSS_SELECTOR,'.formbox__interactive-confirm'
# 密码为空的提示信息
pwd_null_tips = By.CSS_SELECTOR,'.field__tips'
# 登录成功后的退出按钮
quit_login_ok_btn = By.CSS_SELECTOR,'[style="cursor: pointer;"]'
