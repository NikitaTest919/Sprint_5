import pytest
from locators.locators import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestUserLogin:

    def open_login_form(self, driver, base_url):
        driver.get(base_url)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(LOGIN_REGISTRATION_BUTTON)).click()

    def fill_login_form(self, driver, email, password):
        driver.find_element(*LOGIN_EMAIL_INPUT).send_keys(email)
        driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(password)

    def test_login_success(self, driver, base_url):
        self.open_login_form(driver, base_url)
        email = "existing_user@example.com"
        password = "CorrectPassword123!"
        self.fill_login_form(driver, email, password)
        driver.find_element(*LOGIN_BUTTON).click()

        WebDriverWait(driver, 10).until(EC.url_to_be(base_url))
        avatar = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(USER_AVATAR))
        user_name = driver.find_element(*USER_NAME).text

        assert avatar.is_displayed()
        assert user_name == "User"
