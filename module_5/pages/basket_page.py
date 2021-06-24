from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_page(self):
        self.should_be_basket_url()
        self.check_basket_empty_message()
        self.check_basket_not_have_checkout()

    def should_be_basket_url(self):
        assert "basket" in self.browser.current_url, "It is not basket URL!"

    def check_basket_empty_message(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_MESSAGE), "Basket not empty"

    def check_basket_not_have_checkout(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_CHECKOUT_BUTTON), "Basket can be checked out"
