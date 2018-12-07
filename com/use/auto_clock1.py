#coding=utf-8
'''
Created on 2018年9月26日

@author: Pan
'''

import requests
from bs4 import BeautifulSoup
# coding = utf-8

headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
    }

form_data = {
    'username':'pgf',
    'T2':'123'
}

data = requests.get("http://192.168.1.98/szoffice", headers = headers).content
soup = BeautifulSoup(data, 'html.parser')
input_username = soup.find("input", attrs={'class':'s01', 'name':'username'})
input_pwd = soup.find("input", attrs={'class':'s01', 'name':'T2'})
input_username['value'] = 'pgf'
input_pwd['value'] = '123'
print(soup.prettify())