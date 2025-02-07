from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from actions import Actions
import random
import time

class ItemSelection(Actions):
    """Handles item selection, adding to cart, and size selection."""
    def __init__(self, driver, logger):
        super().__init__(driver, logger)
        self.driver = driver
        self.logger = logger

    def select_item_to_purchase(self):
        """Select an item to add to the shopping cart."""
        checkout_urls = ["---", "---"]
        item_number = random.randint(0, len(checkout_urls) - 1)
        self.driver.get(checkout_urls[item_number])
        self.logger.info(f"Selected item: {checkout_urls[item_number]} for purchase")

        try:
            self.add_to_cart()
            self.select_size()
            self.checkout()
        except Exception as e:
            self.logger.error(f"Error during item selection and checkout: {e}")

    def add_to_cart(self):
        """Click the 'Add to Cart' button on the item page."""
        add_to_cart_buttons = [
            "---",
            "---",
        ]

        for add_button in add_to_cart_buttons:
            try:
                self._click_element_by_css_selector(add_button)
                time.sleep(1.43)
                self.logger.info("Item added to cart.")
                break
            except Exception:
                self.logger.warning("Add to Cart button not found!")

    def select_size(self):
        """Select a size for the item."""
        size_selectors = [
            "---",
            "---",
        ]

        for size in size_selectors:
            try:
                size_element = WebDriverWait(self.driver, 2).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, size))
                )
                font_color = size_element.value_of_css_property("color")
                if font_color in ["rgb(0, 0, 0)", "rgba(0, 0, 0, 1)"]:
                    size_element.click()
                    self.logger.info("Size selected.")
                    break
            except Exception:
                self.logger.warning("Size not available.")

    def checkout(self):
        """Proceed to the checkout page."""
        try:
            self.driver.get("---")  # Replace with actual URL
            proceed_to_checkout_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "---"))
            )
            time.sleep(1.84)
            proceed_to_checkout_button.click()
            self.logger.info("Proceeded to checkout.")
            time.sleep(1.81)
        except Exception:
            self.logger.error("Error clicking 'Proceed to Checkout' button.")
