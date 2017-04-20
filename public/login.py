# 登录
def login(self,username,password):
    driver=self.driver
    driver.switch_to_frame("x-URS-iframe")
    driver.find_element_by_xpath('//*[@name="email"]').clear()
    driver.find_element_by_xpath('//*[@name="email"]').send_keys(username)
    driver.find_element_by_xpath('//*[@name="password"]').clear()
    driver.find_element_by_xpath('//*[@name="password"]').send_keys(password)
    driver.find_element_by_id("dologin").click()
# 退出
def logout(self):
    driver=self.driver
    driver.find_element_by_link_text(u"退出").click()

