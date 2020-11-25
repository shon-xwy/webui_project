'''
@Author:shon
'''
from time import sleep

from selenium import webdriver

from page.page_login import PageLogin

driver = webdriver.Chrome()
login = PageLogin(driver)
driver.maximize_window()
driver.get('http://fshon.6868hy.com/')
login.page_click_index_login_btn()
sleep(2)
ele = driver.find_element_by_css_selector('[placeholder="请输入账号"]')
ele.send_keys('ycy888')
sleep(2)


