from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options

class WebDriverManager:
    """Manages the Selenium WebDriver setup and interactions."""
    def __init__(self, driver_path):
        self.driver_path = driver_path
        self.driver = None

    def setup_driver(self):
        """Setup Selenium WebDriver with Edge browser options."""
        edge_options = Options()
        edge_options.add_experimental_option("debuggerAddress", "localhost:2323")

        service = Service(self.driver_path)
        self.driver = webdriver.Edge(service=service, options=edge_options)
        return self.driver

    def quit_driver(self):
        """Quit the WebDriver."""
        if self.driver:
            self.driver.quit()
