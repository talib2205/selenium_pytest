from selenium.webdriver.common.by import By


class DesktopLocators:

    class LoginPageLocators:
        bot_column_div_xpath = (By.XPATH, "//div[@class='bot_column']")
        username_input_xpath = (By.XPATH, '(//input[@id="user-name"])')
        password_input_xpath = (By.XPATH, '(//input[@id="password"])')
        login_button_xpath = (By.XPATH, '(//input[@id="login-button"])')
        invalid_credentials_xpath = (By.XPATH, "//div[@class='error-message-container error']")


