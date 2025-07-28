import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture()
def driver():
    options = Options()
    options.add_argument("--window-size=1920,1080")
    # options.add_argument("--headless")  # Можно раскомментировать для безголового режима
    service = ChromeService()
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

@pytest.fixture()
def base_url():
    return "https://qa-desk.stand.praktikum-services.ru/"
