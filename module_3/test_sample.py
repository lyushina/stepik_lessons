from selenium import webdriver
# Тестовый сценарий 1.1.1. Войти в личный кабинет
# Предусловия:
# Пользователь уже зарегистрирован на сайте
# Шаги:
# 1. Зайти на сайт http://selenium1py.pythonanywhere.com/ru/
# 2. Нажать "Войти или зарегистрироваться" в правом верхнем углу
# 3. В модальном окне ввести адрес электронной почты, который использовался при регистрации
#	Проверка: Валидация email должен содержать символ "@"
# 4. Ввести пароль, который привязан к для данной почты
#	Проверка: пароль должен содержать минимум 9 символов и содержать буквенные значения
# 5. Нажать "Войти"
# Ожидаемый результат:
# #Вход в личный кабинет


main_page_link = "http://selenium1py.pythonanywhere.com/ru/"
search_main_login_link = "login_link"
search_button_css_locator = "input.btn.btn-default"
search_login_username_locator = "id_login-username"
search_login_password_locator = "id_login-password"
input_email = "yushina.larisa@yandex.ru"
input_password = "Hampton+0"


def registered_account_enter():

    browser = webdriver.Chrome()
    try:
        # Arrange
        browser.implicitly_wait(10)
        browser.get(main_page_link)
        # Act
        main_login_link = browser.find_element_by_id(search_main_login_link)
        main_login_link.click()

        login_email = browser.find_element_by_id(search_login_username_locator)
        login_email.send_keys(input_email)
        login_password = browser.find_element_by_id(search_login_password_locator)
        login_password.send_keys(input_password)

        button = browser.find_element_by_css_selector(search_button_css_locator)
        button.click()
        # Assert
        assert '@' in login_email, "Don't have @ in email"
        assert login_password != login_password, "Wrong password"

    finally:
        browser.quit()
