from pages.base_page import BasePage
from utils.logger import get_logger

logger = get_logger()


class CheckoutPage(BasePage):
    # --------------------- LOCATORS ---------------------
    FIRST_NAME = "[data-test='firstName']"
    LAST_NAME = "[data-etst='lastName']"
    POSTAL_CODE = "[data-test='postalCode']"
    CONTINUE_BUTTON = "[data-test='continue']"
    FINISH_BUTTON = "[data-test='finish']"
    SUCCESS_MESSAGE = "[data-test='complete-header']"
    ERROR_MESSAGE = "[data-test='error']"

    # --------------------- ACTIONS ----------------------

    def fill_checkout_info(self, first: str, last: str, postal: str):
        logger.info("Filling checkout information")

        self.fill(self.FIRST_NAME, first)
        self.fill(self.LAST_NAME, last)
        self.fill(self.POSTAL_CODE, postal)

    def continue_checkout(self):
        logger.info("Continuing checkout flow")
        self.click(self.CONTINUE_BUTTON)

    def finish_checkout(self):
        logger.info("Finish checkout")
        self.click(self.FINISH_BUTTON)

    # -------------------- VALIDATIONS -------------------

    def verify_order_success(self):
        logger.info("Verifying order success message")
        self.expect_visible(self.SUCCESS_MESSAGE)

    def verify_error_visible(self):
        logger.info("Verifying checkout validation error")
        self.expect_visible(self.ERROR_MESSAGE)
