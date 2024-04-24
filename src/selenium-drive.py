import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://m.damai.cn/damai/home/index.html')
# 使用 Selenium 完成登录、搜索和预订

print(datetime.datetime.now())

title = driver.title
print(title)




# text_box = driver.find_element(by=By.XPATH, value='//*[@id="damai"]')
grids_button = driver.find_element(by=By.CLASS_NAME, value='home-grids__item')
grids_button.click()

# message = driver.find_element(by=By.CLASS_NAME, value='home-grids__item')
# print(message)
driver.implicitly_wait(10)
print(datetime.datetime.now())