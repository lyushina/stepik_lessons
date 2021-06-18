from .pages.product_page import ProductPage


link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"


class TestProductPage:

    def test_guest_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, link)
        page.open()

        product_title = page.get_product_title()
        product_price = page.get_product_price()
        page.get_cart_amount()
        page.solve_quiz_and_get_code() # почему метод не инициализируется, если есть ссыль на Base page в Product page?

        assert product_title in page.should_be_product_title_in_basket(), 'Wrong product was added'
        assert product_price in page.should_be_cart_amount_in_basket(), 'Wrong cart amount'