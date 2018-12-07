#coding=utf-8
'''
Created on 2018年12月7日

@author: Pan
'''
from splinter.browser import Browser
from time import sleep
import traceback
import time, sys

class hrmis():
    username = 'jccm'
    pwd = 'ESS3BUAT'
    mainUrl = "http://showcase.aishk.com:7701/HRMIS-UAT2/html/login.jsp"
    
    def __init__(self):
        self.driver_name = 'firefox'
        self.executable_path = 'E:/driver/geckodriver'
        self.driver = Browser(driver_name=self.driver_name,executable_path=self.executable_path)
        self.driver.visit(self.mainUrl)
        
    def login(self):
        self.driver.fill('opCNA', self.username)
        self.driver.fill('pwd', self.pwd)
        self.driver.find_by_name('Submit').last.click()
        
    def selectRole(self, role):
        self.driver.find_by_text(role).last.click()   
        
    def convertApp(self, url): 
        '''
            leave '../leave/index.jsp'
        '''
        self.driver.find_link_by_href(url).last().click()
        
if __name__ == '__main__':
    hrmis = hrmis()
    hrmis.login()
    hrmis.selectRole('VTC')
    hrmis.convertApp('../leave/index.jsp')