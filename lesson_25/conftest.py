import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.main_page import MainPage
from pages.registration_page import RegistrationPage

@pytest.fixture(scope="session")
def driver():
    """Ініціалізація браузера"""
    options = Options()
    options.add_argument("--headless=new")  # можна прибрати, якщо хочеш бачити тест
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def open_site(driver):
    """Відкрити сайт з базовою авторизацією"""
    driver.get("https://guest:welcome2qauto@qauto2.forstudy.space")
    return driver


@pytest.fixture
def main_page(driver):
    """Об’єкт головної сторінки (пошук елементів)"""
    return MainPage(driver)


@pytest.fixture
def registration_page(driver):
    """Об’єкт сторінки реєстрації (пошук елементів)"""
    return RegistrationPage(driver)


@pytest.fixture
def go_to_registration(open_site, main_page):
    """Дія: перейти на сторінку реєстрації"""
    open_site
    main_page.sign_up_button.click()
