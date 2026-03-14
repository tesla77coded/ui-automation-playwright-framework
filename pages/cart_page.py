from pages.base_page import BasePage
from utils.logger import get_logger

logger = get_logger()


class CartPage(BasePage):
    # -------------------- LOCATORS ------------------
    CART_ITEM = "[data-test='inventory-item']"
    ITEM_NAME = "[data-test='inventory-item-name']"
    CHECKOUT_BUTTON = "[data-test='checkout']"
    CONTINUE_SHOPPING_BUTTON = "[data-test='conitnue-shopping']"

    # ------------------- ACTIONS --------------------
    def remove_product(self, product_name: str):
        logger.info(f"Removing product from cart: {product_name}")

        product = self.page.locator(self.ITEM_NAME).filter(
            has=self.page.locator(self.ITEM_NAME, has_text=product_name)
        )

        remove_btn = product.locator("button")
        remove_btn.click()

    def continue_shopping(self):
        logger.info("Continuing shopping from cart")
        self.click(self.CONTINUE_SHOPPING_BUTTON)

    def proceed_to_checkout(self):
        logger.info("Proceeding to checkout")
        self.click(self.CHECKOUT_BUTTON)

    # ----------------- VALIDATING ---------------------
    def verify_product_present(self, product_name: str):
        logger.info(f"Verifying product is present: {product_name}")

        product = self.page.locator(self.CART_ITEM).filter(
            has=self.page.locator(self.ITEM_NAME, has_text=product_name)
        )

        product.first.wait_for(state="visible")
