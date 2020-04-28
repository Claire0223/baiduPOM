#-*-coding:utf-8 -*-
import unittest
from HTMLTestRunner import HTMLTestRunner
from testCase.test_BaiduSearch import TestBaiduSearch
import time

if __name__ =='__main__':
    testunit=unittest.TestSuite()
    testunit.addTest(TestBaiduSearch('testSearch'))
 
    newtime=time.strftime('%Y_%m_%d %H-%M-%S')
    filename='D:\\python\\baiduPOM\\commom\\'+' '+ newtime +' '+'result.html'
    fp=open(filename,'w')

    runner=HTMLTestRunner(stream=fp,title='testreport', description='测试用例情况')
    runner.run(testunit)
    fp.close()