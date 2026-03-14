from pages.base_page import BasePage
from utils.logger import get_logger

logger = get_logger()


class InventoryPage(BasePage):
    # ---------- LOCATORS ----------

    SORT_DROPDOWN = "[data-test='product-sort-container']"
    CART_BADGE = "[data-test='shopping-cart-badge']"
    CART_LINK = "[data-test='shopping-cart-link']"
    INVENTORY_ITEM = "[data-test='inventory-item']"
    INVENTORY_ITEM_NAME = "[data-test='inventory-item-name']"

    # ---------- ACTIONS ----------

    def sort_products(self, option_value: str):
        logger.info(f"Sorting products using option: {option_value}")
        self.page.select_option(self.SORT_DROPDOWN, option_value)

    def add_products(self, product_name: str):
        logger.info(f"Adding product to cart: {product_name}")
        product = self.page.locator(self.INVENTORY_ITEM).filter(
            has=self.page.locator(self.INVENTORY_ITEM, has_text=product_name)
        )

        add_btn = product.locator("button")
        add_btn.click()

    def add_multiple_products(self, product_names: list[str]):
        for name in product_names:
            self.add_products(name)

    def go_to_cart(self):
        logger.info("Navigating to cart page")
        self.click(self.CART_LINK)

    # --------- VALIDATION ----------
    def verify_cart_badge_count(self, expected_count: int):
        logger.info(f"Verifying cart badge count = {expected_count}")
        self.expect_text(self.CART_BADGE, str(expected_count))
