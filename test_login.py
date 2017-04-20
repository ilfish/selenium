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

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://mail.163.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_login(self):
        driver = self.driver
        driver.get(self.base_url)
        login.login(self,"yulb1994","zxcvylb1994")
        # driver.switch_to_frame("x-U RS-iframe")
        # driver.find_element_by_xpath('//*[@name="email"]').clear()
        # driver.find_element_by_xpath('//*[@name="email"]').send_keys('yulb1994')
        # driver.find_element_by_xpath('//*[@name="password"]').clear()
        # driver.find_element_by_xpath('//*[@name="password"]').send_keys("zxcvylb1994")
        # driver.find_element_by_id("dologin").click()
        # 获取断言信息进行断言
        text=driver.find_element_by_id('spnUid').text
        self.assertEqual("yulb1994@163.com", text)
        # 退出
        login.logout(self)
        time.sleep(2)
        # driver.find_element_by_link_text(u"退出").click()
    
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
