# -*-coding:utf-8 -*-
from selenium import webdriver
import time,os
import csv  
import unittest
import HTMLTestRunner
csvData=csv.reader(open('login.csv','r'))
Data =[]
#获取csv中每一行的数据（每一行的数据都是一个列表）
for user in csvData:  
    data= []
    for i in user:    #获取每一行的每一个单元格的值（也就是遍历每一行的单元格的值）
        data.append(i)    
    Data.append(data)    #将data的每一个值都添加到Data里面
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
        driver.find_element_by_link_text("安全退出").click()
        time.sleep(2)
        driver.quit()
    #登录-用户名、密码正确登录
    def test_login1(self):
        '''用户名,密码正确登录'''
        username=Data[0][0]
        password=Data[0][1]
        self.user_login(self.driver,username,password)
        time.sleep(2)
        self.driver.quit()
    #用户名正确、密码为空登录
    def test_login2(self):
        '''用户名正确,密码为空登录'''
        username=Data[1][0]
        password=Data[1][1]
        self.user_login(self.driver,username,password)
        time.sleep(2)
        self.driver.quit()
    #用户名正确，密码错误登录
    def test_login3(self):
        '''用户名正确,密码错误登录'''
        username=Data[2][0]
        password=Data[2][1]
        self.user_login(self.driver,username,password)
        time.sleep(2)
        self.driver.quit()
    #用户名错误，密码错误登录
    def test_login4(self):
        '''用户名错误,密码错误登录'''
        username=Data[3][0]
        password=Data[3][1]
        self.user_login(self.driver,username,password)
        time.sleep(2)
        self.driver.quit()
if __name__ == '__main__':
    #unittest.main()
    testreport = unittest.TestSuite()
    testreport.addTest(LoginTest("test_login1"))#可以让测试用例按照指定的顺序执行
    testreport.addTest(LoginTest("test_login2"))
    testreport.addTest(LoginTest("test_login3"))
    testreport.addTest(LoginTest("test_login4"))
    path="C:\Users\Public\Desktop" #定义报告路径
    os.chdir(path)#更换当前工作路径为：path("C:\Users\Public\Desktop")
    ReportName='Result_AutoTest_'+time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))+'.html'
    fp=open(ReportName,'wb')
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title=u"小狗钱钱登录测试报告",description=u"小狗钱钱登录测试详情")
    runner.run(testreport)