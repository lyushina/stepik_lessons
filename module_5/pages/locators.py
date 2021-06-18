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


class ProductPageLocators():
    PRODUCT_TITLE = (By.CSS_SELECTOR, '.product_main h1')
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, '#add_to_basket_form > button')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    CART_AMOUNT = (By.CSS_SELECTOR, '[class="basket-mini pull-right hidden-xs"]')
    BASKET_PRODUCT_TITLE = (By.XPATH, '//*[@id="messages"]/div[1]/div/strong')




