from actions import Actions
import pyautogui
import time

class Login(Actions):
    """Handles the login process."""
    def __init__(self, driver, logger):
        super().__init__(driver, logger)
        self.driver = driver
        self.logger = logger

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
