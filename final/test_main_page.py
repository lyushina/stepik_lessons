import pytest

from .pages.login_page import LoginPage
from .pages.main_page import MainPage
from .pages.basket_page import BasketPage
from .pages.product_page import ProductPage
from .test_product_page import promo_link

link = "http://selenium1py.pythonanywhere.com/"


@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        # Arrange
        page = MainPage(browser, link)
        page.open()
        # Act
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        # Assert
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        # Arrange
        page = MainPage(browser, link)
        # Act
        page.open()
        # Assert
        page.check_login_link()

    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        # Arrange
        page = MainPage(browser, link)
        # Act
        page.open()
        page.go_to_basket_page()
        # Assert
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.check_basket_empty_message()
        basket_page.check_basket_not_have_checkout()


class TestAddToBasketMessages():
    @pytest.mark.xfail
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser, language):
        # Arrange
        promo_page = ProductPage(browser, promo_link)
        promo_page.open()
        # Act
        promo_page.add_to_basket()
        # Assert
        promo_page.should_be_add_to_basket_button()
        promo_page.should_not_be_success_message()

    def test_guest_cant_see_success_message(self, browser, language):
        # Arrange
        promo_page = ProductPage(browser, promo_link)
        # Act
        promo_page.open()
        # Assert
        promo_page.should_not_be_success_message()

    @pytest.mark.xfail
    def test_message_disappeared_after_adding_product_to_basket(self, browser, language):
        # Arrange
        promo_page = ProductPage(browser, promo_link)
        promo_page.open()
        # Act
        promo_page.add_to_basket()
        # Assert
        promo_page.should_be_add_to_basket_button()
        # убедиться, что элемент исчезает в заданный timeout
        promo_page.should_not_be_disappeared_message_after_adding_product_to_basket()
