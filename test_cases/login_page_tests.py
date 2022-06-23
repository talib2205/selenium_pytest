from pytest import mark,fixture
import inspect
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_objects.login_page import LoginPage
from constants.urls import Urls


@mark.all
@mark.login_page
class LoginTests:

    # @mark.current
    def test_load_home_page(self, setup):
        driver = setup['driver']
        browser = setup['browser']
        testcase_name = inspect.stack()[0][3]
        driver.get(Urls.login_page)
        login_page = LoginPage(driver, browser, testcase_name)
        login_page.load_login_page()

    @mark.current
    def test_correct_username_password_value(self, setup):
        driver = setup['driver']
        browser = setup['browser']
        testcase_name = inspect.stack()[0][3]
        driver.get(Urls.login_page)
        login_page = LoginPage(driver, browser, testcase_name)
        login_page.check_correct_username_password_value()
        time.sleep(2)
        assert WebDriverWait(driver, 10).until(EC.url_contains(Urls.home_page))

    @mark.current
    def test_incorrect_username_password_value(self, setup):
        driver = setup['driver']
        browser = setup['browser']
        testcase_name = inspect.stack()[0][3]
        driver.get(Urls.login_page)
        login_page = LoginPage(driver, browser, testcase_name)
        login_page.check_incorrect_username_password_value()

    # def test_search_field_value_check(self, setup):
        # driver.switch_to.window(driver.window_handles[1])








