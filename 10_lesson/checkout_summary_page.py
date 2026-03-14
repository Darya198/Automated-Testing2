import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class CheckoutSummaryPage:
    """Класс для работы с финальной страницей обзора заказа"""

    def __init__(self, driver: WebDriver) -> None:
        """Инициализация драйвера и переход на страницу подтверждения заказа"""
        self._driver = driver
        self._driver.get('https://www.saucedemo.com/checkout-step-two.html')
        self._driver.implicitly_wait(10)
        self._driver.maximize_window()

    @allure.step("Получить итоговую стоимость заказа с экрана")
    def get_total_price(self) -> str:
        """
        Дожидается появления итоговой цены и возвращает её текст

        Returns:
            str: Текст итоговой цены (например, 'Total: $58.29')
        """
        wait = WebDriverWait(self._driver, 50)

        with allure.step("Чтение текста итоговой суммы"):
            price_total_text = wait.until(EC.presence_of_element_located((
                By.CSS_SELECTOR, ".summary_total_label"))).text

        return price_total_text
