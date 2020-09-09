from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        self.should_be_add_button()
        self.click_on_add_button()
        self.should_be_success_added_div()
        self.should_be_basket_info_div()
        self.good_name_equals_added_to_basket_good_name()
        self.good_price_equals_basket_price()

    def should_be_add_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), \
            f"button for selector {ProductPageLocators.ADD_TO_BASKET_BUTTON} is not exist."

    def click_on_add_button(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()

    def should_be_success_added_div(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_ADDED_DIV_NAME), \
            f"div for selector {ProductPageLocators.SUCCESS_ADDED_DIV_NAME} is not exist."

    def should_be_basket_info_div(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_INFO_DIV_PRICE), \
            f"div for selector {ProductPageLocators.BASKET_INFO_DIV_PRICE} is not exist."

    def good_name_equals_added_to_basket_good_name(self):
        good_name = self.browser.find_element(*ProductPageLocators.GOOD_NAME).text
        added_good_name = self.browser.find_element(*ProductPageLocators.SUCCESS_ADDED_DIV_NAME).text
        assert good_name == added_good_name, \
            f"good name ({good_name}) is not equal added to basket good name ({added_good_name})."

    def good_price_equals_basket_price(self):
        good_price = self.browser.find_element(*ProductPageLocators.GOOD_PRICE).text
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_INFO_DIV_PRICE).text
        assert good_price == basket_price, \
            f"good price ({good_price}) is not equal basket price ({basket_price})."

