from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def name_TextBox(context):
    return context.driver.find_element_by_id('i0116')
def next_button(context):
    return context.driver.find_element_by_id('idSIButton9')
def password_TextBox(context):
    return context.driver.find_element_by_id('i0118')
def login_button(context):
    return context.driver.find_element_by_id('idSIButton9')
def wait_name(context):
    WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.ID, 'i0116')))
    return True
def wait_password(context):
    WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.ID, 'i0118')))
    return True