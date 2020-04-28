#-*- coding:utf-8 -*-
import time

class Page(object):
    base_url='http://www.baidu.com'
    def __init__(self,driver,url=base_url):
        self.driver=driver
        self.login_url=url
        self.timeout=30 #超时时长

    #登录
    def loginPage(self,url):
        url=self.login_url
        self.driver.get(url)

    #元素定位
    def findElementPage(self,*loc):
        return self.driver.find_element(*loc)

    #输入文本
    def inputPage(self,loc,text):
        return self.findElementPage(loc).send_keys(text)

    #点击按钮
    def clickPage(self,loc):
        return self.findElementPage(loc).click()

    #获得标题
    def titleGetPage(self):
        return self.driver.title