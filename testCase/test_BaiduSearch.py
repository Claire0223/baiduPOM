#-*- coding:utf-8 -*-
from selenium import webdriver
from pages.searchPage import baiduSearchPage
import time
import unittest

class TestBaiduSearch(unittest.TestCase):

    def setUp(self):
        self.driver=webdriver.Chrome()
    
    def testSearch(self):
        driver=self.driver
        url='http://www.baidu.com'
        text='苏打水'
        
        search_Sudashui=baiduSearchPage(driver)
        search_Sudashui.loginPage(url)
        driver.implicitly_wait(10)

        search_Sudashui.inputSearch(text)
        search_Sudashui.clickButton()
        time.sleep(2)
        driver.get_screenshot_as_file('./苏打水百度搜索.png')


    def tearDown(self):
        self.driver.quit()
