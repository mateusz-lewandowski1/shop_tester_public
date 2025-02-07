import time
import pyautogui
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Actions:
    """Handles actions such as interacting with the website (adding to cart, checkout, etc.)."""
    def __init__(self, driver, logger):
        self.driver = driver
        self.logger = logger

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
