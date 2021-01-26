from selenium import webdriver
import requests
import time

code = input("Input your code")

driver = webdriver.Chrome('/Users/appium/Documents/SeleniumTest/chromedriver')
driver.get("http://127.0.0.1:8080/cw.php")
time.sleep(1)

driver.find_element_by_name('pw').send_keys(code)
time.sleep(1)
driver.find_element_by_name('enter').click()

time.sleep(3)

element = driver.find_elements_by_name("sub")
print(element[0].text)

driver.close()

