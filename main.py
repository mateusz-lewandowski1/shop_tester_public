from bot_config import BotConfig
from webdriver_manager import WebDriverManager
from actions import Actions
from item_selection import ItemSelection
from login import Login
from notification import Notification

class SwiftShopBot:
    """The main bot that orchestrates the entire process."""
    def __init__(self, config, driver_manager, actions, item_selection, login, notification):
        self.config = config
        self.driver_manager = driver_manager
        self.actions = actions
        self.item_selection = item_selection
        self.login = login
        self.notification = notification
        self.emails = self.config.load_emails()

    def main(self, password):
        """Main bot loop."""
        self.driver_manager.setup_driver()

        for email in self.emails:
            try:
                self.item_selection.select_item_to_purchase()
                self.login.login(email, password)
                self.actions.confirm_order()
                self.actions.cancel_order(email)
            except Exception as e:
                self.config.logger.error(f"Error with email {email}: {e}")
            finally:
                self.driver_manager.quit_driver()
