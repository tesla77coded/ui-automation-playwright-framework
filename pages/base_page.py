from playwright.sync_api import Page, expect
from utils.waits_helper import wait_for_element
from utils.logger import get_logger

logger = get_logger()


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    # ------------------ NAVIGATION -----------------

    def navigate(self, url: str):
        logger.info(f"Navigating to {url}")
        self.page.goto(url)

    # ----------------- ACTIONS ---------------------

    def click(self, locator: str):
        logger.info(f"Clicking element: {locator}")
        wait_for_element(self.page, locator)
        self.page.locator(locator).click()

    def fill(self, locator: str, text: str):
        logger.info(f"Filling {locator} with {text}")
        wait_for_element(self.page, locator)
        self.page.locator(locator).fill(text)

    # ----------------- VALIDATIONS -----------------

    def expect_visible(self, locator: str):
        logger.info(f"Expecting element visible: {locator}")
        expect(self.page.locator(locator)).to_be_visible()

    def expect_text(self, locator: str, text: str):
        logger.info(f"Expecting text '{text}' in {locator}")
        expect(self.page.locator(locator)).to_have_text(text)

    def get_text(self, locator: str) -> str:
        wait_for_element(self.page, locator)
        return self.page.locator(locator).inner_text()
