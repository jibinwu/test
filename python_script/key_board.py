#键盘操作（ctrlA,ctrlC,ctrlV）
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

#在百度搜索框输入python,对搜索框进行全选、复制，然后再打开搜狗页面，在搜索框里粘贴，然后搜素，退出
driver=webdriver.Firefox()
driver.get('http://www.baidu.com')
driver.find_element_by_css_selector('#kw').send_keys('python')
driver.find_element_by_css_selector('#kw').send_keys(Keys.CONTROL,'a')
driver.find_element_by_css_selector('#kw').send_keys(Keys.CONTROL,'c')
sleep(2)
driver.get('https://www.sogou.com/')
driver.find_element_by_css_selector('#query').send_keys(Keys.CONTROL,'v')
driver.find_element_by_css_selector('#stb').click()
sleep(2)
driver.quit()
