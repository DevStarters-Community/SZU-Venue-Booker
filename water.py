'''
Author: ztm0929 ztm0929@icloud.com
Date: 2024-03-24 15:32:40
LastEditors: ztm0929 ztm0929@icloud.com
LastEditTime: 2024-03-31 14:53:21
FilePath: \SZU-Venue-Booker\water.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
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
# 这里我们采用更灵活强大的显示等待方式，等待元素加载出来后再进行点击
# time.sleep(3) 无条件等待3秒钟，不推荐这种方式，可能造成时间的浪费，也可能造成元素还未加载完成就进行点击进而报错
# driver.implicitly_wait(10) 作为全局的隐式等待也不推荐，因为可能会影响到后续的操作，不够灵活
# presence_of_element_located 不推荐，我们可以使用更好的 element_to_be_clickable
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="sportVenue"]/div[1]/div/div[1]'))).click()


# 显式等待加载元素，选择对应运动种类并点击
# 这是羽毛球场
# driver.find_element(By.XPATH, '//*[@id="sportVenue"]/div[2]/div[2]/div[2]/div[1]/div/div[1]/div/img').click()

# 这是一楼健身房 ↓
# driver.find_element(By.XPATH, '//*[@id="sportVenue"]/div[2]/div[2]/div[2]/div[7]/div/div[1]/div/img').click()

# 这是篮球场 ↓
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="sportVenue"]/div[2]/div[2]/div[2]/div[5]/div/div[1]/div/img'))).click()

# 显式等待加载元素，选择“次日”并点击
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="apply"]/div[3]/div[4]/div[2]/label/div[2]'))).click()

# 判断次日是否有20:00之后的剩余时间段
# time.sleep(3)
available_time_slots = driver.find_elements(By.XPATH, '//div[@class="element" and contains(@style, "rgb(29, 33, 41)") and (text()="20:00-21:00(可预约)" or text()="21:00-22:00(可预约)")]')
if available_time_slots:
    available_time_slots[0].click()
    # print(available_time_slots)
    # 判断是否有空余的场地并选取第一个
    available_court_slots = driver.find_elements(By.XPATH, '//*[@id="apply"]/div[3]/div[10]/div/label/div[2][contains(@style, "rgb(29, 33, 41)")]')
    if available_court_slots:
        available_court_slots[0].click()
        # 选择“提交预约”并点击
        driver.find_element(By.XPATH, '//*[@id="apply"]/div[3]/div[11]/button[2]').click()
        print(f'已预约成功明天 {available_time_slots[0].text} - {available_court_slots[0].text}，请于45分钟内支付~')

else:
    print("明天20:00后没有可预约的时间段。")
    # 查看今天有无20:00之后的时间段
    driver.find_element(By.XPATH, '//*[@id="apply"]/div[3]/div[4]/div[1]/label/div[2]')
    available_time_slots = driver.find_elements(By.XPATH, '//div[@class="element" and contains(@style, "rgb(29, 33, 41)") and (text()="20:00-21:00(可预约)" or text()="21:00-22:00(可预约)")]')
    if available_time_slots:
        available_time_slots[0].click()
        # 判断是否有空余的场地并选取第一个
        available_court_slots = driver.find_elements(By.XPATH, '//*[@id="apply"]/div[3]/div[10]/div/label/div[2][contains(@style, "rgb(29, 33, 41)")]')
        if available_court_slots:
            available_court_slots[0].click()
            driver.find_element(By.XPATH, '//*[@id="apply"]/div[3]/div[11]/button[2]').click()
            print(f'已预约成功今天 {available_time_slots[0].text} - {available_court_slots[0].text}，请于45分钟内支付~')
    else:
        print("今天20:00后也没有可预约的时间段。")


# 等待3秒钟加载元素，选择“未支付”并点击
# time.sleep(3)
# driver.find_element(By.XPATH, '//*[@id="row0myBookingInfosTable"]/td[1]/a[2]').click()

# 等待3秒钟加载元素，选择“体育经费支付”并点击
# time.sleep(3)
# driver.find_element(By.XPATH, '//*[@id="buttons"]/button[1]').click()


# https://olepay.szu.edu.cn/Order/CreateOrder 这个网址目前没有被添加到校内VPN白名单了
