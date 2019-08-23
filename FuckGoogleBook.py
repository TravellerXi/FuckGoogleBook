#!/usr/bin/env python
# coding:utf-8
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
driverOptions.add_argument(r"user-data-dir=C:\Users\quant\AppData\Local\Google\Chrome\User Data")

driver = webdriver.Chrome("chromedriver",0,driverOptions)
driver.get('https://play.google.com/books/reader?id=sp7fDgAAQBAJ&hl=zh_CN&pg=GBS.PR1')
time.sleep(10)
URL="https://play.google.com/books/reader?id=sp7fDgAAQBAJ&hl=zh_CN&pg=GBS.PA"
PR=160

while (PR<499):
    driver.get(URL+str(PR))
    time.sleep(1)
    # page=driver.find_element_by_id('gb-pagecontrol-input')
    sreach_window = driver.current_window_handle
    time.sleep(3)
    bookname='C:\\Users\\quant\\Desktop\\PDF\\'+'正式'+str(PR)+'.png'
    time.sleep(3)
    driver.get_screenshot_as_file(bookname)
    # fillchange=driver.find_element_by_xpath('//input[@class="gb-pagecontrol-input"]').click()
    # fillchange.clear()
    # fillchange.send_keys('10')
    # fillchange.send_keys(Keys.RETURN)
    #time.sleep(3)
    PR=PR+1
exit()
