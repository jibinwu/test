#下拉菜单操作
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import Select
driver=webdriver.Firefox()
driver.get('http://www.51zxw.net')
# driver.find_element_by_css_selector('[name="username"]').send_keys('心情_1992')
# driver.find_element_by_css_selector('[name="password"]').send_keys('jbw_1992')
# driver.find_element_by_css_selector("[value='2']").click()
# driver.find_element_by_css_selector('[type="submit"]').click()
select=Select(driver.find_element_by_css_selector('[name="CookieDate"]'))
# select.select_by_index(0)
# select.select_by_visible_text('留一天')
select.select_by_value('2')