#-*-coding:utf-8 -*-

from selenium.webdriver.common.by import By
from pages.basePages import Page    #导入基类

class baiduSearchPage(Page):
    
    #定位器
    inputSearchElement=(By.ID,'kw')
    clickButtonElement=(By.ID,'su')

    #Action
    def inputSearch(self,inputText):
        self.driver.find_element(*self.inputSearchElement).send_keys(inputText)
    
    def clickButton(self):
        self.driver.find_element(*self.clickButtonElement).click()
        