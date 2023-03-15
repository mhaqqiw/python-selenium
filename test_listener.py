from selenium.webdriver.common.by import By
from selenium import webdriver
from elements import calc

driver = None

def before_suite():
    print()

def after_suite():
    print()

def before_test():
    global driver
    driver = webdriver.Chrome()
    driver.get("https://www.online-calculator.com/full-screen-calculator/")
    # driver.switch_to.frame(driver.find_element(By.XPATH, calc.iframe_canvas))

def after_test():
    driver.close()