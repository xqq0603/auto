#-*- encoding: UTF-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

from selenium import  webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC  #期望条件
import time
import logging
logging.basicConfig(level=logging.DEBUG,filename='selenium.log',filemode='w',format='%(name)s - %(levelname)s - %(message)s')

driver=webdriver.Chrome('driver/chromedriver.exe')
driver.get("http://www.bing.com")
driver.maximize_window()   #最大化

#assert driver.find_element_by_id('scpl0').text.__contains__('图片')
logging.debug('home page opened')

driver.save_screenshot('screenshot/home.png')  #保存截图
WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID,'sb_form_q')))   #driver ,最长timeout时间。期望条件：元素可点击（用BY方法获取元素）

driver.find_element_by_id('sb_form_q').clear()
driver.find_element_by_xpath('//*[@id="sb_form_q"]').send_keys("selenium")
driver.find_element_by_xpath('//*[@id="sb_form_q"]').screenshot('screenshot/box.png')
driver.find_element_by_xpath('//*[@id="sb_form_q"]').send_keys(Keys.ENTER)   #控制键盘
#driver.find_element_by_xpath('//*[@id="sb_form_go"]').click()

assert "百度百科" in driver.page_source
assert driver.title.__contains__('selenium')

time.sleep(3)

driver.quit()