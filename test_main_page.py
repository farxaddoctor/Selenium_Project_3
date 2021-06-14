from pages.main_page import MainPage
from pages.locators import MainPageLocators
from pages.locators import ProductPageLocators
from pages.locators import CartPageLocators
from pages.login_page import LoginPage
from pages.basket_page import CartPage
from pages.product_page import ProductPage
import pytest


@pytest.mark.login_guest
class TestLoginFromMainPage(object):
    def test_guest_should_see_login_link(self, browser):
        link = MainPageLocators.MAIN_PAGE_LINK
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()

    def test_guest_can_go_to_login_page(self, browser):
        link = MainPageLocators.MAIN_PAGE_LINK
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()


def test_guest_cant_see_product_in_cart_opened_from_main_page(browser):
    link = MainPageLocators.MAIN_PAGE_LINK
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket_page()
    cart_page = CartPage(browser, browser.current_url)
    cart_page.cart_should_be_empty()
