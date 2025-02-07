import time
import random
import logging
import requests
import pyautogui
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SwiftShopBot:
    def __init__(self, driver_path, webhook_url, email_file):
        """Initialize the bot with necessary configuration."""
        self.driver_path = driver_path
        self.webhook_url = webhook_url
        self.email_file = email_file
        self.driver = None
        self.emails = self.load_emails()
        self.setup_logging()

    def setup_logging(self):
        """Setup logging configuration."""
        logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
        self.logger = logging.getLogger(__name__)

    def load_emails(self):
        """Load email addresses from the provided file."""
        try:
            with open(self.email_file, 'r', encoding='utf-8') as file:
                emails = [line.strip() for line in file.readlines()]
            self.logger.info(f"Loaded {len(emails)} email addresses.")
            return emails
        except FileNotFoundError:
            self.logger.error("Email file not found!")
            return []

    def setup_driver(self):
        """Setup Selenium WebDriver with Edge browser options."""
        edge_options = Options()
        edge_options.add_experimental_option("debuggerAddress", "localhost:2323")

        service = Service(self.driver_path)
        self.driver = webdriver.Edge(service=service, options=edge_options)
        self.logger.info("WebDriver successfully set up.")

    def move_mouse(self, x, y, sleep_1, sleep_2):
        """Simulate mouse movement and click at a specified location."""
        pyautogui.moveTo(x, y)
        time.sleep(sleep_1)
        pyautogui.click()
        time.sleep(sleep_2)

    def clear_cookies(self):
        """Manually clear cookies from Swift Shop."""
        self.driver.get("---")  # Replace with actual URL
        time.sleep(2)

        try:
            self._click_element_by_css_selector("---")  # Replace with actual selector
            time.sleep(1)

            self._click_element_by_css_selector("#---")  # Replace with actual selector
            time.sleep(1)
            self.driver.get("---")  # Replace with actual URL
            self.move_mouse(754, 992, 5.153, 1.788)
        except Exception as e:
            self.logger.error(f"Error clearing cookies: {e}")

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
                EC.element_to_be_clickable((By.XPATH, "---"))  # Replace with actual XPath
            )
            time.sleep(1.84)
            proceed_to_checkout_button.click()
            self.logger.info("Proceeded to checkout.")
            time.sleep(1.81)
        except Exception:
            self.logger.error("Error clicking 'Proceed to Checkout' button.")

    def login(self, email, password):
        """Login to Swift Shop account with email and password."""
        self.move_mouse(943, 372, 0.99, 1.98)
        pyautogui.write(email)
        time.sleep(1.1)
        pyautogui.press('enter')

        self.move_mouse(896, 476, 1.02, 2.01)
        pyautogui.write(password)
        time.sleep(0.99)
        pyautogui.press('enter')
        time.sleep(1.82)

    def confirm_order(self):
        """Confirm the order and complete the checkout process."""
        try:
            self._click_element_by_xpath("---")  # Replace with actual XPath
            self.logger.info("Item ordered!")
            time.sleep(3.78)
        except Exception:
            self.logger.error("Error confirming the order.")

    def cancel_order(self, email):
        """Cancel the order if needed."""
        cancel_checkboxes = [
            "---",
            "---",
        ]

        self.driver.get("---")  # Replace with actual URL
        try:
            self._click_element_by_xpath("---")  # Replace with actual XPath
            time.sleep(2.37)

            self._click_element_by_css_selector("---")  # Replace with actual CSS selector
            time.sleep(1.45)

            for checkbox in cancel_checkboxes:
                try:
                    self._click_element_by_xpath(checkbox)
                    time.sleep(1.38)
                    break
                except Exception:
                    self.logger.warning("No checkbox found for cancellation")

            self._click_element_by_xpath("---")  # Replace with actual XPath
            self.logger.info("Order successfully cancelled!")

            # Send notification
            self.send_notification(f"Successfully cancelled the order for account: {email}")
        except Exception:
            self.logger.error("Failed to cancel the order!")
            self.send_notification(f"Failed to cancel the order for account: {email}")

    def send_notification(self, message):
        """Send a notification to the provided Microsoft Teams webhook."""
        payload = {"text": message}  # Format for Microsoft Teams
        try:
            response = requests.post(self.webhook_url, json=payload)
            response.raise_for_status()
            self.logger.info("✅ Notification sent to Microsoft Teams!")
        except requests.exceptions.RequestException as e:
            self.logger.error(f"❌ Error sending notification to Microsoft Teams: {e}")

    def _click_element_by_css_selector(self, selector):
        """Helper function to click an element by CSS selector."""
        element = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, selector))
        )
        element.click()

    def _click_element_by_xpath(self, xpath):
        """Helper function to click an element by XPath."""
        element = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        )
        element.click()

    def main(self, password):
        """Main bot loop."""
        self.setup_driver()

        for email in self.emails:
            try:
                self.select_item_to_purchase()
                self.login(email, password)
                self.confirm_order()
                self.cancel_order(email)
            except Exception as e:
                self.logger.error(f"Error with email {email}: {e}")
            finally:
                self.driver.quit()


if __name__ == "__main__":
    DRIVER_PATH = "msedgedriver.exe"
    WEBHOOK_URL = '---'  # MS Teams webhook URL
    EMAIL_FILE = 'accounts.txt'
    PASSWORD = '---'

    bot = SwiftShopBot(DRIVER_PATH, WEBHOOK_URL, EMAIL_FILE)
    bot.main(PASSWORD)
