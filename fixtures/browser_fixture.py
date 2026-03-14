import pytest
from playwright.sync_api import sync_playwright
from utils.config_reader import get_config
from utils.logger import get_logger

logger = get_logger()


@pytest.fixture(scope="session")
def browser():
    config = get_config()
    headless = config["browser"]["headless"]

    logger.info("Launching browser session")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=headless)
        yield browser
        logger.info("Closing browser session")
        browser.close()


@pytest.fixture(scope="function")
def page(browser):
    logger.info("Creating new browser context and page")
    context = browser.new_context()

    context.tracing.start(screenshots=True, snapshots=True, source=True)
    page = browser.new_page()

    yield page

    logger.info("Closing browser context")
    context.close()
