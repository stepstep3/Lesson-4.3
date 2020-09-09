from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def basket_should_be_empty(self):
        assert self.is_element_present(*BasketPageLocators.CONTINUE_SHOPPING_LINK), "The basket is not empty."

    def basket_should_not_goods(self):
        self.is_not_element_present(*BasketPageLocators.BASKET_SUMMARY_FORM), "There are goods in the basket."
