from selenium.webdriver.common.by import By
from .base_page import BasePage

class RegistrationPage(BasePage):
    """Елементи форми реєстрації"""
    @property
    def first_name(self):
        return self.wait_for_visible((By.ID, "signupName"))

    @property
    def last_name(self):
        return self.wait_for_visible((By.ID, "signupLastName"))

    @property
    def email(self):
        return self.wait_for_visible((By.ID, "signupEmail"))

    @property
    def password(self):
        return self.wait_for_visible((By.ID, "signupPassword"))

    @property
    def repeat_password(self):
        return self.wait_for_visible((By.ID, "signupRepeatPassword"))

    @property
    def register_button(self):
        return self.wait_for_visible((By.XPATH, "//button[text()='Register']"))

    @property
    def success_message(self):
        return self.wait_for_visible((By.CSS_SELECTOR, ".alert-success"))
