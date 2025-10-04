import pytest
from nova_poshta_tracking import NovaPoshtaTrackingPage


@pytest.mark.parametrize("ttn, expected_status", [
    ("20400475838183", "Отримана"),  # приклад ТТН, замінити на реальний
])
def test_tracking_status(ttn, expected_status):
    tracker = NovaPoshtaTrackingPage(headless=False)  # headless=True для фоново
    try:
        tracker.open()
        tracker.enter_ttn(ttn)
        status = tracker.get_status()

        # Додаємо друк для дебагу
        print(f"ТТН: {ttn}")
        print(f"Очікуваний статус: {expected_status}")
        print(f"Отриманий статус: {status}")

        assert status == expected_status, f"Очікуваний статус: {expected_status}, Отриманий: {status}"
    finally:
        tracker.close()

