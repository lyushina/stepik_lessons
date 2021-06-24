from .pages.login_page import LoginPage
from .pages.main_page import MainPage
from .pages.basket_page import BasketPage

link = "http://selenium1py.pythonanywhere.com/"


class TestMainPage:
    def test_guest_can_go_to_login_page(self, browser):
        # Arrange
        page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        # Act
        page.open()  # открываем страницу
        page.go_to_login_page()
        # Assert
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()
        # выполняем метод страницы - переходим на страницу логина

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
        page.go_to_basket()
        # Assert
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.check_basket_empty_message()
        basket_page.check_basket_not_have_checkout()
