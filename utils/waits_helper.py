from playwright.sync_api import Page, TimeoutError as PlaywrightTimeoutError
from utils.logger import get_logger

logger = get_logger()


def wait_for_element(page: Page, locator: str, timeout: int = 5000):
    try:
        page.wait_for_selector(locator, timeout=timeout)
    except PlaywrightTimeoutError:
        logger.error(f"Element not found within timeout: {locator}")
        raise
