import pytest
from selene import browser


@pytest.fixture(scope='function',autouse=True)
def set_browser():
    # глобальные настройки на тест
    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.timeout = 10
    yield
    browser.quit()
