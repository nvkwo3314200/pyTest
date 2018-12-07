#coding=utf-8
'''
Created on 2018年9月26日

@author: Pan
'''

import requests
from bs4 import BeautifulSoup
# coding = utf-8

from selenium import webdriver
import time

browser = webdriver.Firefox()

browser.get("http://192.168.1.98/szoffice")
browser.find_element_by_name("username").clear()     #清空原关键字
browser.find_element_by_name("username").send_keys("pgf")
browser.find_element_by_name("T2").clear()
browser.find_element_by_name("T2").send_keys("123")
browser.find_element_by_name("B1").submit()
time.sleep(2)
browser.quit()
