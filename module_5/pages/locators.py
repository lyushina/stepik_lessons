from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_EMAIL = (By.CSS_SELECTOR, '[name = "login-username"]')
    LOGIN_PASSWORD = (By.CSS_SELECTOR, '[name = "login-password"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '[name = "login_submit"]')
    REG_EMAIL = (By.CSS_SELECTOR, '[name = "registration-email"]')
    REG_PASSWORD = (By.CSS_SELECTOR, '[name = "registration-password1"]')
    REG_PASSWORD_CONFIRM = (By.CSS_SELECTOR, '[name = "registration-password2"]')
    REG_BUTTON = (By.CSS_SELECTOR, '[name = "registration_submit"]')
