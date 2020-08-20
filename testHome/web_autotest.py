from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.common.keys import Keys
class TestSearch:

    # def setUp(self):
    #     self.driver = webdriver.Chrome()

    def test_search_in_python_org(self):
        self.driver=webdriver.Chrome()
        self.driver.get('http://www.python.org')
        assert 'Python' in self.driver.title
        # elm=self.driver.find_element_by_id('id-search-field')
        elm=self.driver.find_element(By.ID,'id-search-field')
        elm.clear()
        elm.send_keys('pycon')
        elm.send_keys(Keys.RETURN)
        assert "No results found." not in self.driver.page_source

        self.driver.close()

    # def tearDown(self):
    #     self.driver.close()



#
# import unittest
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
#
# class PythonOrgSearch(unittest.TestCase):
#
#     def setUp(self):
#         self.driver = webdriver.Chrome()
#
#     def test_search_in_python_org(self):
#         driver = self.driver
#         driver.get("http://www.python.org")
#         self.assertIn("Python", driver.title)
#         elem = driver.find_element_by_name("q")
#         elem.send_keys("pycon")
#         elem.send_keys(Keys.RETURN)
#         assert "No results found." not in driver.page_source
#
#
#     def tearDown(self):
#         self.driver.close()
#
# if __name__ == "__main__":
#     unittest.main()

