import pytest
from locators.locators import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils import generate_unique_email

class TestUserRegistration:

    def open_registration_form(self, driver, base_url):
        driver.get(base_url)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(LOGIN_REGISTRATION_BUTTON)).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(NO_ACCOUNT_BUTTON)).click()

    def fill_registration_form(self, driver, email, password="Password123!", username="User"):
        driver.find_element(*REG_EMAIL_INPUT).send_keys(email)
        driver.find_element(*REG_PASSWORD_INPUT).send_keys(password)
        driver.find_element(*REG_PASSWORD_REPEAT_INPUT).send_keys(password)
        driver.find_element(*REG_USERNAME_INPUT).send_keys(username)

    def test_registration_success(self, driver, base_url):
        self.open_registration_form(driver, base_url)
        email = generate_unique_email()
        self.fill_registration_form(driver, email)
        driver.find_element(*REG_CREATE_ACCOUNT_BUTTON).click()

        # Проверяем переход на главную страницу и отображение аватара и имени
        WebDriverWait(driver, 10).until(EC.url_to_be(base_url))
        avatar = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(USER_AVATAR))
        user_name = driver.find_element(*USER_NAME).text

        assert avatar.is_displayed()
        assert user_name == "User"

    def test_registration_invalid_email(self, driver, base_url):
        self.open_registration_form(driver, base_url)
        driver.find_element(*REG_EMAIL_INPUT).send_keys("invalidemail")
        driver.find_element(*REG_CREATE_ACCOUNT_BUTTON).click()

        email_field = driver.find_element(*REG_EMAIL_INPUT)
        password_field = driver.find_element(*REG_PASSWORD_INPUT)
        password_repeat_field = driver.find_element(*REG_PASSWORD_REPEAT_INPUT)

        # Проверяем, что поля выделены красным (обычно класс с ошибкой)
        assert "error" in email_field.get_attribute("class") or "error" in email_field.get_attribute("aria-invalid")
        assert "error" in password_field.get_attribute("class") or "error" in password_field.get_attribute("aria-invalid")
        assert "error" in password_repeat_field.get_attribute("class") or "error" in password_repeat_field.get_attribute("aria-invalid")

        # Проверяем сообщение "Ошибка" под Email
        error_text = driver.find_element(*REG_EMAIL_ERROR).text
        assert "Ошибка" in error_text

    def test_registration_existing_user(self, driver, base_url):
        self.open_registration_form(driver, base_url)

        # Предполагаем, что user с таким email уже существует
        existing_email = "existing_user@example.com"
        self.fill_registration_form(driver, existing_email)
        driver.find_element(*REG_CREATE_ACCOUNT_BUTTON).click()

        email_field = driver.find_element(*REG_EMAIL_INPUT)
        password_field = driver.find_element(*REG_PASSWORD_INPUT)
        password_repeat_field = driver.find_element(*REG_PASSWORD_REPEAT_INPUT)

        assert "error" in email_field.get_attribute("class") or "error" in email_field.get_attribute("aria-invalid")
        assert "error" in password_field.get_attribute("class") or "error" in password_field.get_attribute("aria-invalid")
        assert "error" in password_repeat_field.get_attribute("class") or "error" in password_repeat_field.get_attribute("aria-invalid")

        error_text = driver.find_element(*REG_EMAIL_ERROR).text
        assert "Ошибка" in error_text
