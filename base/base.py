'''
@Author:shon
'''
import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from tool.get_logger import GetLogger
log = GetLogger().get_logger()


class Base:

    def __init__(self,driver):
        log.info("[base]: 正在获取初始化driver对象:{}".format(driver))
        self.driver = driver

    # 查找一个元素方法
    def base_find_element(self,loc,timeout=30,poll=0.5):
        log.info("[base]: 正在定位：{} 元素，默认定位超时时间为：{}".format(loc,timeout))
        # 使用显示等待 查找元素
        return WebDriverWait(self.driver,timeout=timeout,poll_frequency=poll).until(lambda x: x.find_element(*loc))

    # 查找一组元素方法，返回list
    def base_find_elements(self,loc,timeout=30,poll=0.5):
        return WebDriverWait(self.driver,timeout=timeout,poll_frequency=poll).until(lambda x: x.find_elements(*loc))

    # 点击方法
    def base_click(self,loc):
        log.info("[base]: 正在对:{} 元素实行点击操作 ".format(loc))
        self.base_find_element(loc).click()

    # 输入方法
    def base_input(self,loc,value):
        log.info("[base]: 正在对:{} 元素实行输入操作 ".format(loc))
        el = self.base_find_element(loc)
        # 这里无法使用clear()，改成模拟键盘输入 Ctrl+a 全选后输入新值
        el.send_keys(Keys.CONTROL, 'a')
        el.send_keys(value)

    # 获取文本方法
    def base_get_text(self,loc):
        log.info("[base]: 正在对:{} 元素获取文本操作 ".format(loc))
        return self.base_find_element(loc).text

    # 获取一组文本方法 (获取登录账号 密码为空的时候需要用到)
    def base_get_texts(self,loc,index):
        return self.base_find_elements(loc)[index].text

    # 截图方法
    def base_get_image(self):
        log.info("[base]: 断言错误，调用截图")
        self.driver.get_screenshot_as_file("../image/{}.png".format(time.strftime("%Y_%m_%d %H_%M_%S")))

    # 判断元素是否存在方法
    def base_if_exist(self,loc,timeout=5):
        try:
            self.base_find_element(loc,timeout=timeout)
            log.info("[base]: {}元素查找成功，存在当前页面".format(loc))
            return True
        except:
            log.info("[base]: {}元素查找失败，不存在当前页面".format(loc))
            return False

    # 切换frame表单方法
    def base_switch_frame(self, name):
        self.driver.switch_to.frame(name)

    # 回到默认目录方法
    def base_default_content(self):
        self.driver.switch_to.default_content()

    # 切换窗口 方法 调用此方法
    def base_switch_to_window(self, title):
        log.info("正在执行切换title值为：{}窗口 ".format(title))
        self.driver.switch_to.window(self.base_get_title_handle(title))

    # 获取指定title页面的handle方法
    def base_get_title_handle(self, title):
        # 获取当前页面所有的handles
        for handle in self.driver.window_handles:
            log.info("正在遍历handles：{}-->{}".format(handle, self.driver.window_handles))
            # 切换 handle
            self.driver.switch_to.window(handle)
            log.info("切换 :{} 窗口".format(handle))
            # 获取当前页面title 并判断 是否等于 指定参数title
            log.info("判断当前页面title:{} 是否等于指定的title:{}".format(self.driver.title, title))
            if self.driver.title == title:
                log.info("条件成立！ 返回当前handle{}".format(handle))
                # 返回 handle
                return handle
