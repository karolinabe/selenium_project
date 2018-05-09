#-*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import unittest
from time import sleep

class YahooRegistration(unittest.TestCase):
    def setUp(self):
        # setting up Firefox language preferences
        profile = webdriver.FirefoxProfile()
        profile.set_preference("intl.accept_languages", "en_US")
        self.driver=webdriver.Firefox(profile)
        self.driver=webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("https://www.yahoo.com/")
        self.driver.implicitly_wait(5)

    def test_invalid_username(self):
        driver = self.driver
        register = driver.find_element_by_id("uh-mail-link").click()
        sign_up = driver.find_element_by_id("createacc").click()
        first_name = driver.find_element_by_id("usernamereg-firstName").send_keys("Joanna")
        last_name = driver.find_element_by_id("usernamereg-lastName").send_keys("Pasek")
        email_address = driver.find_element_by_id("usernamereg-yid").send_keys("Joanna$$$")
        password = driver.find_element_by_id("usernamereg-password").send_keys("QWErty123$")
        country_code_choose = driver.find_element_by_xpath("//select[@name='shortCountryCode']/option[165]")
        country_code_choose.location_once_scrolled_into_view
        country_code_choose.click()
        mobile_phone_number = driver.find_element_by_id("usernamereg-phone").send_keys("789789890")
        birth_month = Select(driver.find_element_by_id("usernamereg-month")).select_by_value("7")
        birth_day = driver.find_element_by_id("usernamereg-day").send_keys("28")
        birth_year = driver.find_element_by_id("usernamereg-year").send_keys("1987")
        gender = driver.find_element_by_id("usernamereg-freeformGender").click()
        gender_choose = driver.find_element_by_xpath('//ul[@id="reg-gender-list"]/li[1]').click()
        continue_button = driver.find_element_by_id("reg-submit-button").click()
        error_notice = driver.find_element_by_id("reg-error-yid")
        print(error_notice.text.encode('utf-8'))
        self.assertEqual(error_notice.text, u"You can only use letters, numbers, periods (‘.’), and underscores (‘_’) in your username.")
        sleep(5)

    def tearDown(self):
        self.driver.quit()

if __name__=="__main__":
    unittest.main(verbosity=2)
