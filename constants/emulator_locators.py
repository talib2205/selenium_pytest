from selenium.webdriver.common.by import By


class EmulatorLocators:

    class LoginPageLocators:
        bot_column_div_xpath = (By.XPATH, "//div[@class='bot_column']")
        main_search_input_xpath = (By.XPATH, '(//input[@id="search_query_top"])')

