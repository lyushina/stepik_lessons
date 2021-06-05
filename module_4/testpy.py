import pytest
from selenium import webdriver


@pytest.fixture()
def test_page1(self):
    link = 'http://suninjuly.github.io/registration1.html'
    browser = webdriver.Chrome()
    browser.get(link)
    elements = browser.find_elements_by_xpath("//input[@required]")
    for element in elements:
        element.send_keys("Мой ответ")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text
    self.assertEqual(welcome_text, welcome_text_elt, "Congratulations! You have successfully registered!")

    browser.quit()


@pytest.fixture()
def test_page2(self):
    link = 'http://suninjuly.github.io/registration2.html'
    browser = webdriver.Chrome()
    browser.get(link)
    elements = browser.find_elements_by_xpath("//input[@required]")
    for element in elements:
        element.send_keys("Мой ответ")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text
    self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", 'Wrong')

    browser.quit()
