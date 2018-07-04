#-*-coding:utf-8-*-

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
import os

'''
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

#查询、添加cookie

sreach_windows=driver.current_window_handle
time.sleep(1)

driver.add_cookie({'name':'Tai','value':'shuai'})
for cookie in driver.get_cookies():
        print("添加后的cookie是  %s》%s"%(cookie['name'],cookie['value']))
        
class DL():#工具
    def Wait(self,time,element):#显示等待
        try:
            print('元素加载, 页面等待中 ...')
            WebDriverWait(driver, time).until(EC.presence_of_element_located(element))
            user = driver.find_element_by_id("loginname")
            sleep(3)
            user.clear()
            user.send_keys('278159453@qq.com')
            pwd = driver.find_element_by_name("password")
            sleep(3)
            pwd.clear()
            pwd.send_keys("ZQT951753")
            dl = driver.find_element_by_xpath(
                "/html/body/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[2]/div[1]/div[2]/div[1]/div/div/div/div[3]/div[6]")
            sleep(1)
            dl.click()
            sleep(3)
        except NoSuchElementException:
            print('元素异常，已截图')
            driver.save_screenshot('异常截图/screenshot.png')
        driver.quit()
driver=webdriver.Firefox()
driver.maximize_window()
driver.get('https://weibo.com')
locator=(By.ID,'loginname')

#link=driver.find_element_by_link_text("设置")
#ActionChains(driver).move_to_element(link).perform()
# 等待直到元素出现, 点击
gj=DL()
gj.Wait(1,locator)'''

driver=webdriver.Firefox()
driver.maximize_window()
driver.get("https://im.qq.com/download")
locator=(By.ID,'imedit_wordandurl_pctabdownurl')
sleep(5)

try:
    print('元素加载, 页面等待中 ...')
    WebDriverWait(driver,15).until(EC.presence_of_element_located(locator))
    driver.find_element_by_id("imedit_wordandurl_pctabdownurl").click()
    #driver.find_element_by_id('stfile').send_keys(r'C:\Users\lenovo\Desktop\WX\07bd023b5bb5c9ea2688da5cd039b6003af3b338.jpg')
    sleep(5)
except:
    print('元素异常')
driver.quit()






