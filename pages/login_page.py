from pages import base_page
from pages.base_page import BasePage
from utils.config_reader import get_config
from utils.logger import get_logger

logger = get_logger()


class LoginPage(BasePage):
    # -------------- LOCATORS -------------------
    USERNAME_INPUT = "[data-test='username']"
    PASSWORD_INPUT = "[data-test='password']"
    LOGIN_BUTTON = "[data-test='login-button']"
    ERROR_MESSAGE = "[data-test='error']"

    # -------------- ACTIONS --------------------
    def load(self):
        config = get_config()
        base_url = config["app"]["base_url"]
        self.navigate(base_url)

    def login(self, username: str, password: str):
        logger.info(f"Attempting login for user: {username}")
        self.fill(self.USERNAME_INPUT, username)
        self.fill(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    # -------------- VALIDATIONS -----------------
    def verify_login_failed(self):
        logger.info("Verifying login failure message is visible")
        self.expect_visible(self.ERROR_MESSAGE)

    def get_error_text(self) -> str:
        return self.get_text(self.ERROR_MESSAGE)
