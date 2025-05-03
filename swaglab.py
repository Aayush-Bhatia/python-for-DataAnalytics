from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
url = 'https://www.saucedemo.com/v1/'
driver.get(url)
time.sleep(3)

element  = driver.find_element(By.ID , 'user_name')
element.send_keys('problem_user')

element  = driver.find_element(By.ID , 'password')
element.send_keys('secret_sauce')

element  = driver.find_element(By.NAME , 'login_button')
element.click()

time.sleep(3)