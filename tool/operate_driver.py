'''
@Author:shon
打开和关闭浏览器
'''
from selenium import webdriver

import page


class OperateDriver:

    driver = None

    @classmethod
    def get_driver(cls):
        if cls.driver is None:
            # 获取驱动对象
            cls.driver = webdriver.Chrome()
            # 最大化浏览器
            cls.driver.maximize_window()
            # 打开url
            cls.driver.get(page.URL)
        # 返回浏览器
        return cls.driver

    @classmethod
    def close_driver(cls):
        if cls.driver:
            cls.driver.quit()
            # 必须置空  （因为单单quit，还存在driver对象地址）
            cls.driver = None