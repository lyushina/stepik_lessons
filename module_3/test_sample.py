import time

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver


try:
    #открытие страницы
    browser: WebDriver = webdriver.Chrome()
    browser.get("http://selenium1py.pythonanywhere.com/ru/")
    time.sleep(3)
    #выбрать селектор и нажать на кнопку
    enter = browser.find_element_by_id('login_link')
    enter.click()
    #введение данных для логина

    login_email = browser.find_element_by_id('id_login-username')
    login_email.send_keys('yushina.larisa@yandex.ru')
    assert 'youremail@mail.com' in login_email

    login_password = browser.find_element_by_id('id_login-password')
    login_password.send_keys('Hampton+0')
    assert len(login_password) == 9
    #я не нашла как проверять буквенные значения

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:

    time.sleep(3)
    browser.quit()



