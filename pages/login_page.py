rom.base_page
import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        substring = LoginPageLocators.SUBSTRING_LOGIN
        assert substring in self.browser.current_url, "No 'login' in url on this page!"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "No login form on page!"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "No register form on page!"

    def make_email_and_pass(self):
      
        return (str(time.time()) + "farxd@mail.ru", "password")

    def register_new_user(self, email, password):
       
        self.email = email
        self.password = password

        email_input = self.browser.find_element(*LoginPageLocators.EMAIL_ADDR_INPUT)
        pass_input = self.browser.find_element(*LoginPageLocators.PASSWORD1_INPUT)
        pass_confirm = self.browser.find_element(*LoginPageLocators.PASSWORD2_INPUT)
        reg_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)

     
        email_input.send_keys(email)
        pass_input.send_keys(password)
        pass_confirm.send_keys(password)

        reg_button.click()
