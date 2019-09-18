from selenium import webdriver
from time import sleep

'''
# driver=webdriver.Chrome() #创建一个chrome驱动对象
driver=webdriver.Firefox() #创建一个Firefox驱动对象
driver.get('http://www.51zxw.net')
driver.maximize_window()
print(driver.title)
sleep(2)

driver.get('http://www.baidu.com')
driver.set_window_size(400,800)
print(driver.title)
driver.refresh()
sleep(3)

driver.back()
sleep(2)
driver.forward()
sleep(3)
driver.quit()'''
#元素定位id与name
# driver=webdriver.Firefox()
# driver.get('http://www.baidu.com')
# driver.maximize_window()
# #driver.find_element_by_id('kw').send_keys('selenium')
# driver.find_element_by_name('wd').send_keys('selenium')
# driver.find_element_by_id('su').click()
# sleep(3)
# driver.back()
# driver.set_window_size(500, 500)
# sleep(2)
# driver.quit()
#元素定位Tag_name
# driver=webdriver.Firefox()
# driver.get('http://wxxtest.jbx188.com/index')
# driver.find_elements_by_tag_name('input')[0].send_keys('心情_1992')
# driver.find_elements_by_tag_name('input')[1].send_keys('jbw_1992')
# sleep(2)
# driver.quit()
#元素定位class_name
driver=webdriver.Firefox()
driver.get('http://wxxtest.jbx188.com/index')
driver.find_element_by_css_selector('[placeholder="请输入车辆牌照"]').send_keys('66666')
driver.find_element_by_css_selector('[placeholder="请输入车主姓名"]').send_keys('测试')
driver.find_element_by_css_selector('#telPhone').send_keys('13800138000')
driver.find_element_by_css_selector('.index-form-btn').click()
driver.find_element_by_xpath('//input[@id="framecode"]').send_keys('LBV8A1408HMJ67708')
driver.find_element_by_css_selector('[placeholder="请选择品牌型号"]').click()
driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[3]/div/ul/li[17]/div[2]').click()
driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div[2]/ul/li[2]/div[2]').click()
driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div[4]/div[55]/ul/li/p[1]')
driver.find_element_by_xpath('//input[@id="engineno"]').send_keys('A447D226')
driver.find_element_by_css_selector('[placeholder="请选择注册日期"]').send_keys('2017-09-15')
driver.find_element_by_css_selector('.btn-nobottom').click()

# driver.find_element_by_css_selector('[type="button"]').click()
# driver.find_element_by_class_name('telephone-inp inp').send_keys('13800138000')
# driver.find_element_by_class_name('index-form-btn btn').click()
# sleep(3)
# driver.quit()


