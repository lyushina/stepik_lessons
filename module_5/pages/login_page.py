from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Incorrect login URL"
        assert True

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL), "Login email field is not allocated"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), "Login Password field is not allocated"
        assert self.is_element_present(*LoginPageLocators.LOGIN_BUTTON), "Login submit button is not allocated"
        assert True

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REG_EMAIL), "Registration email field is not allocated"
        assert self.is_element_present(*LoginPageLocators.REG_PASSWORD), "Registration Password field is not allocated"
        assert self.is_element_present(
            *LoginPageLocators.REG_PASSWORD_CONFIRM), "Registration Password confirm field is not allocated"
        assert self.is_element_present(*LoginPageLocators.REG_BUTTON), "Registration submit button is not allocated"
        assert True

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.REG_EMAIL)
        email_field.send_keys(email)
        password_field = self.browser.find_element(*LoginPageLocators.REG_PASSWORD)
        password_field.send_keys(password)
        confirm_password_field = self.browser.find_element(*LoginPageLocators.REG_PASSWORD_CONFIRM)
        confirm_password_field.send_keys(password)
        submit_button = self.browser.find_element(*LoginPageLocators.REG_BUTTON)
        submit_button.click()


