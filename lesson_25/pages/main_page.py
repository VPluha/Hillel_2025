from selenium.webdriver.common.by import By
from .base_page import BasePage

class MainPage(BasePage):
    """Елементи головної сторінки"""
    @property
    def sign_up_button(self):
        return self.wait_for_visible((By.XPATH, "//button[text()='Sign up']"))
