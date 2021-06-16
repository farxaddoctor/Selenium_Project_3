import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome', help="Choose browser: firefox or chrome")
    parser.addoption('--language', action='store', default=None, help="Say language name to select")


@pytest.fixture(scope="function")
def browser(request):
    choosen_language = request.config.getoption("language")
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        opts = Options()
        opts.add_experimental_option('prefs', {'intl.accept_languages': choosen_language})
        opts.add_experimental_option('w3c', False)
        browser = webdriver.Chrome(options=opts)
    elif browser_name == "firefox":
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", choosen_language)
        browser = webdriver.Firefox(firefox_profile=fp)
    yield browser
    browser.quit()
