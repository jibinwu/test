import unittest
import time
from ddt import ddt, data, unpack
from appium import webdriver
import os

@ddt
class MyTestCase(unittest.TestCase):
    # @classmethod
    def setUp(self):
        caps = {"platformName": "Android",
                "deviceName": "9889d539424d324a4d",
                "appPackage": "com.lianxing.purchase.mock",
                "appActivity": "com.lianxing.purchase.mall.launcher.LauncherActivity",
                "unicodeKeyboard": "true",
                "resetKeyboard": "true",
                # "autoGrantPermissions":"true"  授予应用权限
                }

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    @data(("15058321650", "123456a", False),("15000000000", "123456a", True))
    @unpack
    def test_login(self, username, password, expected):
        self.driver.find_element_by_id("android:id/button1").click()
        self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
        self.driver.find_element_by_xpath("//*[contains(@resource-id,'iv_cancel')]").click()
        time.sleep(3)
        self.driver.swipe(1400, 500, 100, 500)
        self.driver.swipe(1400, 500, 100, 500)
        self.driver.get_screenshot_as_file(time.ctime()+".png")
        self.driver.find_element_by_id("com.lianxing.purchase.mock:id/btn_join").click()
        self.driver.find_element_by_id("com.lianxing.purchase.mock:id/edit_username").clear()
        self.driver.find_element_by_id("com.lianxing.purchase.mock:id/edit_username").send_keys(username)
        self.driver.find_element_by_id("com.lianxing.purchase.mock:id/edit_password").clear()
        self.driver.find_element_by_id("com.lianxing.purchase.mock:id/edit_password").send_keys(password)
        self.driver.find_element_by_id("com.lianxing.purchase.mock:id/btn_login").click()
        time.sleep(3)

        try:
            if self.driver.find_element_by_id("com.lianxing.purchase.mock:id/btn_login").is_displayed():
                test = True
        except Exception as e:
            test = False

        self.assertEqual(test, expected)

    # @classmethod
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
