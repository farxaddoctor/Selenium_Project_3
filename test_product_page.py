from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators
from .pages.locators import LoginPageLocators
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import CartPage
import pytest



@pytest.mark.auth_user
class TestUserAddToCartFromProductPage(object):

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser, timeout=5):
        link = LoginPageLocators.LOGIN_PAGE_LINK  # ссылка на страницу логина\регистрации
        self.browser = browser
        self.browser.implicitly_wait(timeout)
        page = LoginPage(browser, link)
        page.open()
        email, password = page.make_email_and_pass()
        page.register_new_user(email, password)
        page.should_be_authorized_user()  

    @pytest.mark.need_review
    def test_user_can_add_product_to_cart(self, browser):
        link = ProductPageLocators.PRODUCT_PAGE_PROMO

        # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page = ProductPage(browser, link)

        # открываем нужную страницу
        page.open()

        bookToCompare = page.find_book_name()
        priceToCompare = page.find_book_price()

        # добавляем товар в корзину
        page.add_item_to_cart()

        page.solve_quiz_and_get_code()
        page.right_book_and_right_price_message(bookToCompare, priceToCompare)

    def test_user_cant_see_success_message(self, browser):
        link = ProductPageLocators.PRODUCT_PAGE_LINK

        # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page = ProductPage(browser, link)

        # открываем нужную страницу
        page.open()
        page.should_not_be_success_message()


@pytest.mark.need_review
def test_guest_can_add_product_to_cart(browser):
    link = ProductPageLocators.PRODUCT_PAGE_PROMO

    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page = ProductPage(browser, link)

    # открываем нужную страницу
    page.open()

    bookToCompare = page.find_book_name()
    priceToCompare = page.find_book_price()

    # добавляем товар в корзину
    page.add_item_to_cart()

    page.solve_quiz_and_get_code()
    # проверяем, что название и цена книги верные
    page.right_book_and_right_price_message(bookToCompare, priceToCompare)


def test_guest_should_see_login_link_on_product_page(browser):
    # проверка, что пользователь "видит" кнопку логина на странице продукта
    link = ProductPageLocators.PRODUCT_PAGE_LINK
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    # проверка, что пользователь может перейти на страницу логина со страницы продукта
    link = ProductPageLocators.PRODUCT_PAGE_LINK
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_cart_opened_from_product_page(browser):
    link = ProductPageLocators.PRODUCT_PAGE_LINK
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket_page()
    cart_page = CartPage(browser, browser.current_url)
    cart_page.cart_should_be_empty()
