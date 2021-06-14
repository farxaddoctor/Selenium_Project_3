from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import CartPageLocators

class CartPage(BasePage):
    def cart_should_be_empty(self):
        self.shouldnt_be_any_product_in_a_cart()
        self.should_be_empty_cart_text_on_basket_page()

    def shouldnt_be_any_product_in_a_cart(self):
        substring = CartPageLocators.SUBSTRING_BASKET_EN_GB
        assert substring in self.browser.find_element(*CartPageLocators.BASKET_EMPTY).text, "No message of empty basket!"

    def should_be_empty_cart_text_on_basket_page(self):
        assert self.is_not_element_present(*CartPageLocators.BASKET_NOT_EMPTY), "Basket is not empty, but it should!"

    def should_be_not_cart_text_on_basket_page(self):
        assert self.is_element_present(*CartPageLocators.BASKET_NOT_EMPTY), "Basket is empty, but it shouldn't!"
