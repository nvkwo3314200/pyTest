# coding = utf-8
from selenium import webdriver
import time

url = 'http://showcase.aishk.com:7701/HRMIS-UAT2/'
browser = webdriver.Firefox()
browser.get(url)
time.sleep(2)
browser.find_element_by_id("opCNA").clear();
browser.find_element_by_id("opCNA").send_keys("jccm");
browser.find_element_by_name("pwd").clear();
browser.find_element_by_name("pwd").send_keys("ESS3BUAT");
browser.find_element_by_name("Submit").submit();
