import time
import pytest
from pages.basket_page import BasketPage
from pages.product_page import ProductPage
from pages.login_page import LoginPage

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
promo_link = "?promo="


@pytest.mark.login_guest
class TestLoginFromProductPage():
    def test_guest_should_see_login_link_on_product_page(self, browser):
        # Arrange
        page = ProductPage(browser, link)
        # Act
        page.open()
        # Assert
        page.check_login_link()

    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        # Arrange
        page = ProductPage(browser, link)
        page.open()
        # Act
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        # Assert
        login_page.check_login_link()


class TestProductPage:
    @pytest.mark.parametrize('promo_offer',
                             ["offer0", "offer1", "offer2", "offer3", "offer4", "offer5", "offer6",
                              pytest.param("offer7", marks=pytest.mark.xfail),
                              "offer8", "offer9"])
    def test_guest_can_add_product_to_basket(self, browser, promo_offer):
        # Arrange
        page = ProductPage(browser, link + promo_link + promo_offer)
        page.open()
        # Act
        product_title = page.get_product_title()
        page.get_product_price()
        page.add_to_basket()
        page.solve_quiz_and_get_code()
        # Assert
        page.check_success_alert_present()
        page.check_product_and_alert_same()
        page.check_product_and_basket_price_same()


@pytest.mark.empty_basket
class TestProductPage:
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser, language):
        # Arrange
        page = ProductPage(browser, link)
        page.open()
        # Act
        page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)
        # Assert
        basket_page.should_be_basket_page()


@pytest.mark.add_to_basket
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    # Arrange
    def setup(self, browser):
        self.page = LoginPage(browser, link)
        self.page.open()
        self.page.go_to_login_page()
        email = str(time.time()) + "@mail.com"
        password = "Passw0rd1!!"
        self.page.register_new_user(email, password)
        self.page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        promo_page = ProductPage(browser, link)
        # Act
        promo_page.open()
        # Assert
        promo_page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, browser, language):
        # Arrange
        promo_page = ProductPage(browser, link)
        promo_page.open()
        # Act
        promo_page.add_to_basket()
        # Assert
        promo_page.should_be_add_to_basket_button()
