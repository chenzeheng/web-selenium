# -*-coding:utf-8 -*-
from selenium import webdriver
import time,os 
import unittest
import HTMLTestRunner

class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver= webdriver.Firefox()
        self.driver.get("http://www.xgqq.com")
    #登录
    def user_login(self,driver,username,password): 
        self.driver.find_element_by_css_selector("a[class=g-login-btn]").click()
        self.driver.find_element_by_name("name").send_keys(username)
        self.driver.find_element_by_name("password").send_keys(password)
        self.driver.find_element_by_id("ui-dialog-login-btn-submit").click()
    #退出
    def user_logout(self,driver):
        self.driver.find_element_by_link_text("安全退出").click()
        time.sleep(2)
        driver.quit()
    #登录-用户名、密码正确登录
    def test_login1(self):
        '''用户名,密码正确登录'''
        self.user_login(self.driver,"186xxx","xxx")
        time.sleep(2)
        self.driver.quit()
    #用户名正确、密码为空登录
    def test_login2(self):
        '''用户名正确,密码为空登录'''
        self.user_login(self.driver,"186xxx","")
        time.sleep(2)
        self.driver.quit()
    #用户名正确，密码错误登录
    def test_login3(self):
        '''用户名正确,密码错误登录'''
        self.user_login(self.driver,"186xxx","22")
        time.sleep(2)
        self.driver.quit()
    #用户名错误，密码正确登录
    def test_login4(self):
        '''用户名错误,密码正确登录'''
        self.user_login(self.driver,"18xxx","xxx")
        time.sleep(2)
        self.driver.quit()
     #用户名为空，密码为空登录
    def test_login5(self):
        '''用户名为空，密码为空登录'''
        self.user_login(self.driver,"","")
        time.sleep(2)
        self.driver.quit()
if __name__ == '__main__':
    #unittest.main()
    testreport = unittest.TestSuite()
    testreport.addTest(LoginTest("test_login1"))#可以让测试用例按照指定的顺序执行
    testreport.addTest(LoginTest("test_login2"))
    testreport.addTest(LoginTest("test_login3"))
    testreport.addTest(LoginTest("test_login4"))
    testreport.addTest(LoginTest("test_login5"))
    path=u"D:\自动化资料报告" #定义报告路径
    os.chdir(path)#更换当前工作路径为：path("D:\自动化资料报告")
    ReportName='Result_AutoTest_'+time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))+'.html'
    fp=open(ReportName,'wb')
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title=u"小狗钱钱登录测试报告",description=u"小狗钱钱登录测试详情")
    runner.run(testreport)
    fp.close()
