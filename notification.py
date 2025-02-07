import requests

class Notification:
    """Handles sending notifications to Microsoft Teams."""
    def __init__(self, webhook_url, logger):
        self.webhook_url = webhook_url
        self.logger = logger

    def send_notification(self, message):
        """Send a notification to the provided Microsoft Teams webhook."""
        payload = {"text": message}  # Format for Microsoft Teams
        try:
            response = requests.post(self.webhook_url, json=payload)
            response.raise_for_status()
            self.logger.info("✅ Notification sent to Microsoft Teams!")
        except requests.exceptions.RequestException as e:
            self.logger.error(f"❌ Error sending notification to Microsoft Teams: {e}")
