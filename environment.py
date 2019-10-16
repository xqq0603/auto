#-*- encoding: UTF-8 -*-
from selenium import  webdriver

def before_all(context):
    context.driver=webdriver.Chrome('driver/chromedriver.exe')
    pass
def before_feature(context,feature):
    print 'before feature'
    pass
def before_scenario(context,scenario):
    pass
def before_step(context,step):
    pass


def after_all(context):
    context.driver.quit()
    pass