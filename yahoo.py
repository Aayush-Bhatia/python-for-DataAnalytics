from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
url = 'https://in.search.yahoo.com/?fr2=inr'

driver.get(url)

element = driver.find_element(By.NAME,'p')
element.send_keys('Hello Word')

time.sleep(3)


element = driver.find_element(By.NAME,'p')
element.send_keys(Keys.RETURN)

time.sleep(5)