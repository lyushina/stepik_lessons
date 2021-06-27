from selenium.webdriver.common.by import By


class BasePageLocators():
    BASKET_LINK = (By.CSS_SELECTOR,".basket-mini :nth-child(1).btn.btn-default")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class MainPageLocators(BasePageLocators):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators(BasePageLocators):
    LOGIN_EMAIL = (By.CSS_SELECTOR, '[name = "login-username"]')
    LOGIN_PASSWORD = (By.CSS_SELECTOR, '[name = "login-password"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '[name = "login_submit"]')
    REG_EMAIL = (By.CSS_SELECTOR, '[name = "registration-email"]')
    REG_PASSWORD = (By.CSS_SELECTOR, '[name = "registration-password1"]')
    REG_PASSWORD_CONFIRM = (By.CSS_SELECTOR, '[name = "registration-password2"]')
    REG_BUTTON = (By.CSS_SELECTOR, '[name = "registration_submit"]')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class ProductPageLocators(BasePageLocators):
    PRODUCT_TITLE = (By.CSS_SELECTOR, '.product_main h1')
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, '#add_to_basket_form > button')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    CART_AMOUNT = (By.CSS_SELECTOR, '[class="basket-mini pull-right hidden-xs"]')
    BASKET_PRODUCT_TITLE = (By.XPATH, '//*[@id="messages"]/div[1]/div/strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-success .alertinner")
    BASKET_SUCCESS_ALERT = (By.CSS_SELECTOR, '#messages .alert:nth-child(1)')
    BASKET_TOTAL_ALERT = (By.CSS_SELECTOR, '#messages .alert:nth-child(3)')
    BASKET_TOTAL_PRICE = (By.CSS_SELECTOR, '#messages .alert:nth-child(3) strong')
    VIEW_BASKET_FROM_ALERT = (By.CSS_SELECTOR, '.alertinner p a:nth-child(1)')
    CHECKOUT_NOW_FROM_ALERT = (By.CSS_SELECTOR, '.alertinner p a:nth-child(2)')


class BasketPageLocators(BasePageLocators):
    BASKET_ALERT = (By.CSS_SELECTOR, '.alertinner')
    BASKET_CONTENT = (By.CSS_SELECTOR, '.content > #content_inner')
    BASKET_VIEW_BASKET_BUTTON = (By.CSS_SELECTOR, 'p:nth-child(2) >a:nth-child(1)')
    BASKET_CHECKOUT_BUTTON = (By.CSS_SELECTOR, 'p:nth-child(2) >a:nth-child(2)')
    BASKET_ORDER_TOTAL = (By.CSS_SELECTOR, '.total > .price_color')
    BASKET_EMPTY_MESSAGE = (By.CSS_SELECTOR, '#content_inner > p:nth-child(1)')
