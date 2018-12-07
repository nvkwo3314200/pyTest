#coding=utf-8
'''
Created on 2018年10月15日

@author: Pan
'''
from splinter.browser import Browser
from time import sleep
import traceback
import time, sys

class huoche(object):
    driver_name = ''
    executable_path = ''
    #用户名，密码
    username = u"nvkwo38647"
    passwd = u"3286541Nv"
    # cookies值得自己去找, 下面两个分别是沈阳, 哈尔滨
    #starts = u"%u6C88%u9633%2CSYT"
    #ends = u"%u54C8%u5C14%u6EE8%2CHBB"
    
    starts = u'%u6DF1%u5733%2CSZQ' #深圳
    ends = u'%u6CC9%u5DDE%2CQYS' #泉州
    
    starts = u'%u5E7F%u5DDE%2CGZQ' #广州
    ends = u'%u677E%u6ECB%2CSIN' #松滋
    # 时间格式2018-01-19
    dtime = u"2018-12-16"
    # 车次，选择第几趟，0则从上之下依次点击
    order = 1
    ###乘客名
    #users = [u"潘高峰",u"陈成"]
    users = [u"潘高峰"]
    ##席位
    xb = u"二等座"
    yw = u"硬卧";
    yz = u"硬座";
    pz = u"成人票"
    xw = yz
    
    frequency = 1;
    
    tryTime = 10
    
    """网址"""
    ticket_url = "https://kyfw.12306.cn/otn/leftTicket/init"
    login_url = "https://kyfw.12306.cn/otn/login/init"
    initmy_url = "https://kyfw.12306.cn/otn/view/index.html"
    buy = "https://kyfw.12306.cn/otn/confirmPassenger/initDc"
    
    def __init__(self):
        self.driver_name = 'firefox'
        self.executable_path = 'E:/driver/geckodriver'

    def login(self):
        self.driver.visit(self.login_url)
        self.driver.fill("loginUserDTO.user_name", self.username)
        # sleep(1)
        self.driver.fill("userDTO.password", self.passwd)
        print(u"等待验证码，自行输入...")
        while True:
            print(self.driver.url)
            if self.driver.url != self.initmy_url:
                sleep(1)
            else:
                break

    def start(self):
        self.driver = Browser(driver_name=self.driver_name,executable_path=self.executable_path)
        self.driver.driver.set_window_size(1400, 1000)
        self.login()
        # sleep(1)
        self.driver.visit(self.ticket_url)
        try:
            print(u"购票页面开始...")
            # sleep(1)
            # 加载查询信息
            self.driver.cookies.add({"_jc_save_fromStation": self.starts})
            self.driver.cookies.add({"_jc_save_toStation": self.ends})
            self.driver.cookies.add({"_jc_save_fromDate": self.dtime})
            self.driver.reload()

            count = 0
            if self.order != 0:
                while self.driver.url == self.ticket_url:
                    try:
                        self.driver.find_by_text(u"查询").click()
                        count += 1
                        print(u"循环点击查询... 第 %s 次" % count)
                        sleep(self.frequency)
                        self.driver.find_by_text(u"预订")[self.order - 1].click()
                    except Exception as e:
                        print(e)
                        print(u"还没开始预订")
                        continue
            else:
                while self.driver.url == self.ticket_url:
                    self.driver.find_by_text(u"查询").click()
                    count += 1
                    print(u"循环点击查询... 第 %s 次" % count)
                    sleep(0.8 * self.frequency)
                    try:
                        for i in self.driver.find_by_text(u"预订"):
                            i.click()
                            sleep(1)
                    except Exception as e:
                        print(e)
                        print(u"还没开始预订 %s" % count)
                        continue
            print(u"开始预订...")
            # sleep(3)
            # self.driver.reload()
            sleep(1)
            print(u'开始选择用户...')
            for user in self.users:
                self.driver.find_by_text(user).last.click()

            
            sleep(1)
            
            i = 0
            while True:
                if i > self.tryTime:
                    break
                i += 1
                try:
                    #self.driver.find_by_text(self.pz).click()
                    #self.driver.find_by_id('ticketType_1').select(self.pz)
                    # sleep(1)
                    
                    self.driver.find_by_id('seatType_1').select(self.xw)
                    self.driver.select('seatType_1', '3')
                    #self.driver.find_by_text(self.xw).click()
                    break
                except Exception as e:
                    print(e)
             
            print(u"提交订单...")   
            isClick = False
            while not isClick:
                try:
                    self.driver.find_by_id('submitOrder_id').click()
                except Exception as e:
                    print(e)
                    
            try:
                print(u"开始选座...")
                self.driver.find_by_id('1D').last.click()
                self.driver.find_by_id('1F').last.click()
            except Exception as e:
                print(e)
            print(u"确认选座...")
            #self.driver.find_by_id('qr_submit_id').click()
            
            while True:
                try:
                    self.driver.find_by_id('qr_submit_id').click()
                    self.driver.find_by_text(u'确认').click()
                    break
                except Exception as e:
                    print(e)    
        except Exception as e:
            print(e)

if __name__ == '__main__':
    huoche = huoche()
    huoche.start()