import pytest
from selene.support.shared import browser
from selenium.webdriver.chrome.options import Options
from selene import Browser, Config


@pytest.fixture(scope="function")
def setup_chrome():
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {"enableVNC": True, "enableVideo": True},
    }
    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options,
    )


browser = Browser(Config(driver))
yield browser