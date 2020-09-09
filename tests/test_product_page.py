import pytest
from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.locators import ProductPageLocators
import time


MAIN_LINK = "http://selenium1py.pythonanywhere.com/"
PRODUCT_LINK = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, browser):
        page = LoginPage(browser, MAIN_LINK)
        page.open()
        page.go_to_login_page()
        page.should_be_register_form()
        email = str(time.time()) + "@chtogdekogda.com"
        password = "1234567890qwerty"
        page.register_new_user(email, password)
        page.should_be_authorized_user()
        # time.sleep(5)

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, PRODUCT_LINK)
        page.open()
        page.add_product_to_basket()
        # time.sleep(5)

    @pytest.mark.skip
    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, PRODUCT_LINK)
        page.open()
        page.is_not_element_present(*ProductPageLocators.SUCCESS_ADDED_DIV)


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, PRODUCT_LINK)
    page.open()
    page.add_product_to_basket()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = BasketPage(browser, PRODUCT_LINK)
    page.open()
    page.should_be_basket_link()
    page.go_to_basket()
    page.basket_should_not_goods()
    page.basket_should_be_empty()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, PRODUCT_LINK)
    page.open()
    page.go_to_login_page()


# ------------------ TEST FROM LAST TOPIC, UNUSED IN FINAL PROJECT ---------------------


@pytest.mark.skip
@pytest.mark.parametrize('link', [
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
    pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                 marks=pytest.mark.xfail),
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
])
def test_guest_add_good_to_basket(browser, link):
    try:
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket()
    except AssertionError:
        assert False, f"failed link: {link}"


@pytest.mark.skip
@pytest.mark.parametrize("link", ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"])
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.is_not_element_present(*ProductPageLocators.SUCCESS_ADDED_DIV)


@pytest.mark.skip
@pytest.mark.parametrize("link", ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"])
def test_guest_cant_see_success_message(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.is_not_element_present(*ProductPageLocators.SUCCESS_ADDED_DIV)


@pytest.mark.skip
@pytest.mark.parametrize("link", ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"])
def test_message_disappeared_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.is_disappeared(*ProductPageLocators.SUCCESS_ADDED_DIV)


@pytest.mark.skip
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
