import pytest
from locators.locators import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestUserLogout:

    def login(self, driver, base_url, email, password):
        driver.get(base_url)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(LOGIN_REGISTRATION_BUTTON)).click()
        driver.find_element(*LOGIN_EMAIL_INPUT).send_keys(email)
        driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(password)
        driver.find_element(*LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(USER_AVATAR))

    def test_logout_success(self, driver, base_url):
        email = "existing_user@example.com"
        password = "CorrectPassword123!"

        self.login(driver, base_url, email, password)
        driver.find_element(*LOGOUT_BUTTON).click()

        # Проверяем, что аватар и имя пользователя отсутствуют
        # и появилась кнопка "Вход и регистрация"
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LOGIN_REGISTRATION_BUTTON))
        assert len(driver.find_elements(*USER_AVATAR)) == 0
        assert len(driver.find_elements(*USER_NAME)) == 0
