"""
Написати тест, який перевіяє процес реєстрації користувача в системі https://qauto2.forstudy.space/
Використовувати PageObject-и тільки для пошуку елементів.
PageObject-и повинні логічно співвідностись з частинами програми.
Для взаємодії з елементами використовувати фікстури.
Тести можуть використовувати ТІЛЬКИ фікстури.
Дані для входу на сайт -
login - guest
pass - welcome2qauto
Для доступу через селеніум можна використати наступну конструкцію - driver.get("<https://UserName:Password@qauto2.forstudy.space>;");
"""

import pytest
import random

@pytest.mark.usefixtures("go_to_registration")
def test_user_registration(driver, registration_page):
    """Перевіряє успішну реєстрацію нового користувача"""

    # Унікальний email
    email = f"test_user_{random.randint(1000,9999)}@mail.com"

    # Заповнення полів
    registration_page.first_name.send_keys("Vasyl")
    registration_page.last_name.send_keys("Pliukhin")
    registration_page.email.send_keys(email)
    registration_page.password.send_keys("Qwerty123!")
    registration_page.repeat_password.send_keys("Qwerty123!")
    registration_page.register_button.click()

    # Перевірка повідомлення про успішну реєстрацію
    success = registration_page.success_message.text
    assert "Registration complete" in success or "successfully" in success.lower()
