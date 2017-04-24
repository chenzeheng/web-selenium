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
    #登录测试用例1
    def test_login1(self):
        '''用户名、密码正确登录'''
        username=Data[0][0]
        password=Data[0][1]
        self.user_login(self.driver,username,password)
        time.sleep(2)
        self.driver.quit()
if __name__ == '__main__':
    #unittest.main()
    testreport = unittest.TestSuite()
    testreport.addTest(LoginTest("test_login1"))
    path="C:\Users\Public\Desktop" #定义报告路径
    os.chdir(path)#更换当前工作路径为：path("C:\Users\Public\Desktop")
    ReportName='Result_AutoTest_'+time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))+'.html'
    fp=open(ReportName,'wb')
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title="Test Report",description="Test Result Detail")
    runner.run(testreport)