import pytest
from locators.locators import *
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from utils import generate_unique_email

class TestCreateAd:

    def login(self, driver, base_url, email, password):
        driver.get(base_url)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(LOGIN_REGISTRATION_BUTTON)).click()
        driver.find_element(*LOGIN_EMAIL_INPUT).send_keys(email)
        driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(password)
        driver.find_element(*LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(USER_AVATAR))

    def test_create_ad_not_authorized(self, driver, base_url):
        driver.get(base_url)
        driver.find_element(*CREATE_AD_BUTTON).click()
        modal_title = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(CREATE_AD_MODAL_TITLE)).text
        assert modal_title == "Чтобы разместить объявление, авторизуйтесь"

    def test_create_ad_authorized(self, driver, base_url):
        email = "existing_user@example.com"
        password = "CorrectPassword123!"

        self.login(driver, base_url, email, password)

        driver.find_element(*CREATE_AD_BUTTON).click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(AD_TITLE_INPUT)).send_keys("Тестовое объявление")
        driver.find_element(*AD_DESCRIPTION_INPUT).send_keys("Описание тестового товара")
        driver.find_element(*AD_PRICE_INPUT).send_keys("1000")

        # Выбор из Dropdown (Select)
        category_select = Select(driver.find_element(*AD_CATEGORY_DROPDOWN))
        category_select.select_by_index(1)  # выбираем первый доступный вариант (кроме заголовка)

        city_select = Select(driver.find_element(*AD_CITY_DROPDOWN))
        city_select.select_by_index(1)

        # Выбор radio button "Состояние товара"
        driver.find_element(*AD_CONDITION_RADIO_NEW).click()

        driver.find_element(*AD_PUBLISH_BUTTON).click()

        # Переходим в профиль
        driver.find_element(*PROFILE_BUTTON).click()

        # Проверяем, что объявление отображается в блоке "Мои объявления"
        ads = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located(MY_ADS_TITLES))
        titles = [ad.text for ad in ads]

        assert "Тестовое объявление" in titles
