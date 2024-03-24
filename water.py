from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from dotenv import load_dotenv
import os

load_dotenv()
username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')

# 打开Chrome 并 直接进入场馆预约的界面
driver = webdriver.Chrome()
driver.get("https://ehall.szu.edu.cn/qljfwapp/sys/lwSzuCgyy/index.do#/sportVenue")


# 自动进入的情况下，需要先输入账号密码并点击登录按钮
driver.find_element(By.XPATH, '//*[@id="username"]').send_keys(username)
driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
driver.find_element(By.XPATH, '//*[@id="casLoginForm"]/p[5]/button').click()

# 等待3秒钟加载元素，选择“粤海校区”并点击
time.sleep(3)
driver.find_element(By.XPATH, '//*[@id="sportVenue"]/div[1]/div/div[1]').click()

# 等待3秒钟加载元素，选择“篮球”并点击
time.sleep(3)
driver.find_element(By.XPATH, '//*[@id="sportVenue"]/div[2]/div[2]/div[2]/div[5]/div/div[1]/div/img').click()

# 等待3秒钟加载元素，选择“当天19:00-20:00”并点击
time.sleep(3)
driver.find_element(By.XPATH, '//*[@id="apply"]/div[3]/div[6]/div[12]/label/div[2]').click()

# 等待3秒钟加载元素，选择“东馆室内篮球场”并点击
time.sleep(3)
driver.find_element(By.XPATH, '//*[@id="apply"]/div[3]/div[8]/div[3]').click()

# 等待3秒钟加载元素，选择“4号篮球场”并点击
time.sleep(3)
driver.find_element(By.XPATH, '//*[@id="apply"]/div[3]/div[10]/div[4]/label/div[2]').click()

# 等待3秒钟加载元素，选择“提交预约”并点击
time.sleep(3)
driver.find_element(By.XPATH, '//*[@id="apply"]/div[3]/div[11]/button[2]').click()

# 等待3秒钟加载元素，选择“未支付”并点击
time.sleep(3)
driver.find_element(By.XPATH, '//*[@id="row0myBookingInfosTable"]/td[1]/a[2]').click()

# 等待3秒钟加载元素，选择“体育经费支付”并点击
time.sleep(3)
driver.find_element(By.XPATH, '//*[@id="buttons"]/button[1]').click()

# https://olepay.szu.edu.cn/Order/CreateOrder 这个网址目前没有被添加到校内VPN白名单了

time.sleep(60)