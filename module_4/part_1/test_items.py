from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Data
link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
expected_button_text = {'ru': 'Добавить в корзину',
                        'en-gb': 'Add to basket',
                        'es': 'Añadir al carrito',
                        'fr': 'Ajouter au panier'}


def test_add_to_basket_local(browser, language):
    # Arrange
    browser.get(link)
    # Act
    basket_button = browser.find_element_by_css_selector('.btn-add-to-basket')
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(basket_button))
    page_lang = browser.find_element_by_css_selector('[class="no-js"]').get_attribute(language)

    # Assert
    assert basket_button.text in expected_button_text[language], "Неверный язык кнопки"
    assert page_lang == language, "Неверное наименование кнопки"
