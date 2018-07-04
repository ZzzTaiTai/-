#-*-coding:utf-8-*-
from selenium import webdriver
driver.maximize_window()
print("设置浏览器大小")
driver=webdriver.Chrome()
one='http://www.baidu.com'
print("现在地址是%s"%(one))
driver.get(one)

two='http://news.baidu.com'
print("现在是%s"%(two))
driver.get(two)


print("返回到%s"%(one))
driver.back()

driver.quit()
