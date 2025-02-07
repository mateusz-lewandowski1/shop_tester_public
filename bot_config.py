import logging

class BotConfig:
    """Handles bot configuration and logging setup."""
    def __init__(self, driver_path, webhook_url, email_file):
        self.driver_path = driver_path
        self.webhook_url = webhook_url
        self.email_file = email_file
        self.logger = self.setup_logging()

    def setup_logging(self):
        """Setup logging configuration."""
        logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
        return logging.getLogger(__name__)

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
          
