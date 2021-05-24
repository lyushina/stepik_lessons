import math
import time
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser: WebDriver = webdriver.Chrome()
    browser.get(" http://suninjuly.github.io/get_attribute.html")
    time.sleep(5)

    value = browser.find_element_by_css_selector('img[id="treasure"]')
    number = value.get_attribute("valuex")
    assert number is not None, 'Number is not selected by default'
    x = number.valuex
    y = calc(x)

    search = browser.find_element_by_id('answer')
    search.send_keys(y)

    option1 = browser.find_element_by_id('robotCheckbox')
    option1.click()
    option1 = browser.find_element_by_id('robotsRule')
    option1.click()
    button = browser.find_element_by_css_selector('button.btn')
    button.click()

finally:

    time.sleep(5)
    browser.quit()
