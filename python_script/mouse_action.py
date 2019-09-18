#鼠标操作（双击、右击、悬停）
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
driver=webdriver.Firefox()
driver.get('http://www.baidu.com')
driver.find_element_by_css_selector('#kw').send_keys('python')
# driver.find_element_by_css_selector('#su').click()
obj=driver.find_element_by_css_selector('#kw')
ActionChains(driver).double_click(obj).perform()
sleep(2)
ActionChains(driver).context_click(obj).perform()
sleep(2)
above=driver.find_element_by_css_selector('.pf')
ActionChains(driver).move_to_element(above).perform()

