import pytest
from selene.support.shared import browser


@pytest.fixture(scope='session', autouse=True)
def browser_management():
    browser.open("https://demoqa.com/automation-practice-form")
