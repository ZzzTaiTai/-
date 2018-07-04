#-*-coding:utf-8-*-

from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
'''from selenium import webdriver

driver=webdriver.Ie()
driver.get("https://www.baidu.com")
driver.find_element_by_id("kw").send_keys("Selenium2")
driver.find_element_by_id("su").click()
driver.quit()
print("现在的地址是%s"%(first_url))
driver.get(first_url)

seconds_url='http://news.baidu.com'
print("现在的地址是%s"%(seconds_url))
driver.get(seconds_url)

print("后退到%s"%(first_url))
driver.back()

print("前进到%s"%(seconds_url))
driver.forward()

driver.refresh()
print("刷新了")

print("登录之前")
title=driver.title
print(title)
now_url=driver.current_url
print(now_url)
frame=driver.find_element(By.ID,"login_frame")
driver.switch_to.frame(frame)

driver.find_element(By.ID,"switcher_plogin").click()
zh=driver.find_element(By.NAME,"u")
zh.send_keys("337290074")
mm=driver.find_element(By.NAME,"p")
mm.send_keys("ZQT951753")
time.sleep(2)
driver.find_element(By.ID,"login_button").click()
print("登录完成后")
title=driver.title
print(title)
now_url=driver.current_url
print(now_url)




'''
driver=webdriver.Firefox()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get('https://news.baidu.com')
sreach_windows=driver.current_window_handle
time.sleep(1)

driver.add_cookie({'name':'Tai','value':'shuai'})
for cookie in driver.get_cookies():
        print("添加后的cookie是  %s》%s"%(cookie['name'],cookie['value']))
time.sleep(1)



driver.quit()



