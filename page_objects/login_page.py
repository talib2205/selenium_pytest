import time
from constants.locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver, browser, testcase_name):
        self.driver = driver
        self.testcase_name = testcase_name
        self.browser = browser
        self.locator = Locators(driver).locators.HomePageLocators

    def load_login_page(self):
        bot_column = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located(self.locator.bot_column_div_xpath))

    def check_correct_username_password_value(self):
        username_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.locator.username_input_xpath))
        username_field.send_keys("standard_user")
        time.sleep(0.5)
        passwowrd_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.locator.password_input_xpath))
        passwowrd_field.send_keys("secret_sauce")
        time.sleep(0.5)
        login_btn = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.locator.login_button_xpath))
        self.driver.execute_script('arguments[0].click()', login_btn)

    def check_incorrect_username_password_value(self):
        username_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.locator.username_input_xpath))
        username_field.send_keys("standard_user12")
        time.sleep(0.5)
        passwowrd_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.locator.password_input_xpath))
        passwowrd_field.send_keys("secret_sauce564")
        time.sleep(0.5)
        login_btn = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.locator.login_button_xpath))
        self.driver.execute_script('arguments[0].click()', login_btn)
        time.sleep(0.5)
        error_message = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.locator.invalid_credentials_xpath))
