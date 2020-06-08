#!/usr/bin/env python3
# coding:utf-8
#author:https://github.com/TravellerXi
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver.support.ui import Select
import time
import os
driverOptions = webdriver.ChromeOptions()
driverOptions.add_argument(r"user-data-dir=C:\Users\quant\AppData\Local\Google\Chrome\User Data")#较为重要，读取Chrome浏览器已登录用户的profie。
#否则，在selenium驱动的情况下，googleBook无法登录。
#现在，既然能加载profile，那么先登录GoogleBook再加载selenium即可。

#PR 和PA一个是前言部分一个是正文。
driver = webdriver.Chrome("chromedriver",0,driverOptions)
driver.get('https://play.google.com/books/reader?id=sp7fDgAAQBAJ&hl=zh_CN&pg=GBS.PR1')
#URL是当前GoogleBook浏览的URL
time.sleep(10)
URL="https://play.google.com/books/reader?id=sp7fDgAAQBAJ&hl=zh_CN&pg=GBS.PA"
PR=160

#理论上，针对PR和PA，都可以使用以下函数来获取，不过多说明，只留一个函数

while (PR<499):
    driver.get(URL+str(PR))
    time.sleep(1)
    # page=driver.find_element_by_id('gb-pagecontrol-input')
    sreach_window = driver.current_window_handle
    time.sleep(3)
    bookname='C:\\Users\\quant\\Desktop\\PDF\\'+'正式'+str(PR)+'.png' #file location
    time.sleep(3)
    driver.get_screenshot_as_file(bookname)
    PR=PR+1
exit()
