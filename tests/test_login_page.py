from pages.login_page import LoginPage


LINK = "http://selenium1py.pythonanywhere.com/accounts/login/"


def test_correct_login_url(browser):
    page = LoginPage(browser, LINK)
    page.open()
    page.should_be_login_url()


def test_exist_login_form(browser):
    page = LoginPage(browser, LINK)
    page.open()
    page.should_be_login_form()


def test_exist_register_form(browser):
    page = LoginPage(browser, LINK)
    page.open()
    page.should_be_register_form()
