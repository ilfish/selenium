# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from public import login
import xml.dom.minidom

dom=xml.dom.minidom.parse("E:\Temp\\test_case\\test_data\login.xml")
root=dom.documentElement

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        logins=root.getElementsByTagName('url')
        self.base_url = logins[0].firstChild.data
        self.verificationErrors = []
        self.accept_next_alert = True

    # 用户名、密码为空
    def test_null(self):
        driver=self.driver
        driver.get(self.base_url)
        logins=root.getElementsByTagName('null')
        # 获得null标签的username、password属性值
        username=logins[0].getAttribute("username")
        password=logins[0].getAttribute("password")
        prompt_info=logins[0].firstChild.data
        # 登录
        login.login(self,username,password)
        # 获取断言信息进行断言
        text=driver.find_element_by_xpath('//*[@class="m-nerror err_email"]').text
        self.assertEqual(text,prompt_info)


    # 输入用户名、密码为空
    def pawd_null(self):
        driver=self.driver
        driver.get(self.base_url)
        logins=root.getElementsByTagName('pawd_null')
        username=logins[0].getAttribute("username")
        password=logins[0].getAttribute("password")
        prompt_info=logins[0].firstChild.data
        login.login(self,username,password)
        text=driver.find_element_by_xpath('//*[@class="m-nerror err_password"]').text
        self.assertEqual(prompt_info,text)


    # 用户名为空、只输入密码
    def user_null(self):
        driver=self.driver
        driver.get(self.base_url)
        logins=root.getElementsByTagName("user_null")
        username=logins[0].getAttribute("username")
        password=logins[0].getAttribute("password")
        prompt_info=logins[0].firstChild.data
        login.login(self,username,password)
        text=driver.find_element_by_xpath('//*[@class="m-nerror err_email"]').text
        self.assertEqual(prompt_info,text)


    # 用户名密码错误
    def error(self):
        driver=self.driver
        driver.get(self.base_url)
        logins=root.getElementsByTagName("error")
        username=logins[0].getAttribute("username")
        password=logins[0].getAttribute("password")
        prompt_info=logins[0].firstChild.data
        login.login(self,username,password)
        text=driver.find_element_by_xpath('//*[@class="m-nerror"]').text
        self.assertEqual(prompt_info,text)



    # def test_login(self):
    #     driver = self.driver
    #     driver.get(self.base_url)
    #     login.login(self,"yulb1994","zxcvylb1994")
    #     # 获取断言信息进行断言
    #     text=driver.find_element_by_id('spnUid').text
    #     self.assertEqual("yulb1994@163.com", text)
    #     # 退出
    #     login.logout(self)
    #     time.sleep(2)

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True

    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
