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

if __name__ == "__main__":
    DRIVER_PATH = "msedgedriver.exe"
    WEBHOOK_URL = '---'  # MS Teams
    EMAIL_FILE = 'accounts.txt'
    PASSWORD = '---'

    config = BotConfig(DRIVER_PATH, WEBHOOK_URL, EMAIL_FILE)

    driver_manager = WebDriverManager(DRIVER_PATH)
    actions = Actions(driver_manager.driver, config.logger)
    item_selection = ItemSelection(driver_manager.driver, config.logger)
    login = Login(driver_manager.driver, config.logger)
    notification = Notification(WEBHOOK_URL, config.logger)

    bot = SwiftShopBot(config, driver_manager, actions, item_selection, login, notification)

    bot.main(PASSWORD)
