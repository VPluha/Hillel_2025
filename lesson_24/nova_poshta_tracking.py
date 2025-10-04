from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class NovaPoshtaTrackingPage:
    def __init__(self, headless=True):
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
        self.driver = webdriver.Chrome(options=options)
        self.wait = WebDriverWait(self.driver, 15)

    def open(self):
        self.driver.get("https://tracking.novaposhta.ua/")

    def enter_ttn(self, ttn):
        input_box = self.wait.until(
            EC.visibility_of_element_located((By.ID, "en"))
        )
        input_box.clear()
        input_box.send_keys(ttn)
        input_box.submit()  # або натиснення Enter

    def get_status(self):
        # Чекаємо на появу статусу
        status_container = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.header__status-text"))
        )
        return status_container.text.strip()

    def close(self):
        self.driver.quit()
