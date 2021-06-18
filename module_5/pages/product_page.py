from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        link.click()

    def get_product_title(self):
        product_title = self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE)
        return product_title.text

    def get_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        return product_price.text

    def get_product_title_in_basket(self):
        product_title_in_basket = self.browser.find_element(*ProductPageLocators.BASKET_PRODUCT_TITLE)
        return product_title_in_basket.text

    def get_cart_amount(self):
        cart_amount_in_basket = self.browser.find_element(*ProductPageLocators.CART_AMOUNT)
        return cart_amount_in_basket.text

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(
            *ProductPageLocators.ADD_TO_BASKET_BUTTON), 'Add to BASKET button is not presented'

    def should_be_product_title(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_TITLE), 'Product title is not presented'

    def should_be_product_price(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), 'Product price is not presented'

    def should_be_product_title_in_basket(self):
        assert self.is_element_present(
            *ProductPageLocators.BASKET_PRODUCT_TITLE), "Product is not the same in the basket"

    def should_be_cart_amount_in_basket(self):
        assert self.is_element_present(*ProductPageLocators.CART_AMOUNT), "Cart amount is not the same in the basket"
