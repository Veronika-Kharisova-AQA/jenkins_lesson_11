import pytest
from selene import browser

from utils import attach


@pytest.fixture(scope='session', autouse=True)
def browser_setup():
    browser.config.driver_name = 'chrome'
    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_width = '1280'
    browser.config.window_height = '900'
    browser.config.timeout = 6

    yield
    # ATTACHMENTS
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    browser.quit()