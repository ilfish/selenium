from selenium import webdriver
import unittest
import time
from public import login
import xml.dom.minidom

# 打开xml文档
dom=xml.dom.minidom.parse("E:\Temp\\test_case\\test_data\login.xml")
# 获得文档元素对象
root=dom.documentElement

class TestSendMail(unittest.TestCase):
    def SetUp(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        logins=root.getElementsByTagName('url')
        self.base_url = logins[0].firstChild.data
        self.verificationErrors = []
        self.accept_next_alert = True


    # 只输入收件人发送邮件
    def test_send_mail(self):
        driver=self.driver
        driver.get(self.base_url)
        # 登录
        login.login(self,"yulb1994","zxcvylb1994")
        # 写信
        driver.find_element_by_xpath('//*[@class="js-component-component ra0 mD0"]').click()
        # 填写收件人
        driver.find_element_by_xpath('//*[@class="js-component-emailcontainer nui-multiLineIpt C-multiLineIpt nui-ipt"]').clear()
        driver.find_element_by_xpath('//*[@class="js-component-emailcontainer nui-multiLineIpt C-multiLineIpt nui-ipt"]').send_keys("601963559@qq.com")
        # 发送邮件
        driver.find_element_by_xpath('//*[@class="nui-btn-icon"]/span[1]').click()
        driver.find_element_by_xpath('//*[@class="nui-btn-text"]/span').click()
        # 断言发送结果
        text=driver.find_element_by_xpath('//*[@class="nui-ico se0 pv1"]/b').text
        self.assertEqual(text,u'发送成功')
        time.sleep(5)
        login.logout(self)


    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__=='__main__':
    unittest.main()
