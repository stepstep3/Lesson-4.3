from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert ("login" in self.browser.current_url), f"'login' phrase is not present in the url: {self.url} "

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), f"login form for selector " \
            f"{LoginPageLocators.LOGIN_FORM} is not exist"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), f"register form for selector " \
            f"{LoginPageLocators.REGISTER_FORM} is not exist"
        assert self.is_element_present(*LoginPageLocators.REGISTER_EMAIL), f"register email field for selector " \
            f"{LoginPageLocators.REGISTER_EMAIL} is not exist"
        assert self.is_element_present(*LoginPageLocators.REGISTER_PASSWORD), f"register password field for selector " \
            f"{LoginPageLocators.REGISTER_PASSWORD} is not exist"
        assert self.is_element_present(*LoginPageLocators.REGISTER_CONFIRM_PASSWORD), f"register password confirm " \
            f"field for selector {LoginPageLocators.REGISTER_CONFIRM_PASSWORD} is not exist"
        assert self.is_element_present(*LoginPageLocators.REGISTER_BUTTON), f"register button for selector " \
            f"{LoginPageLocators.REGISTER_BUTTON} is not exist"

    def register_new_user(self, email, password):
        try:
            email_field = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
            password_field = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD)
            confirm_password_field = self.browser.find_element(*LoginPageLocators.REGISTER_CONFIRM_PASSWORD)
            register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
            email_field.send_keys(email)
            password_field.send_keys(password)
            confirm_password_field.send_keys(password)
            register_button.click()
        except Exception as e:
            assert False, f"Registration failed. Error info: {e}"
