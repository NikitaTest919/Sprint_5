from selenium.webdriver.common.by import By

# Главная страница
LOGIN_REGISTRATION_BUTTON = (By.XPATH, "//button[contains(text(),'Вход и регистрация')]")
CREATE_AD_BUTTON = (By.XPATH, "//button[contains(text(),'Разместить объявление')]")
USER_AVATAR = (By.CSS_SELECTOR, "img.user-avatar")
USER_NAME = (By.CSS_SELECTOR, "div.user-name")

# Модальное окно регистрации/входа
NO_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(text(),'Нет аккаунта')]")

# Поля регистрации
REG_EMAIL_INPUT = (By.NAME, "email")
REG_PASSWORD_INPUT = (By.NAME, "password")
REG_PASSWORD_REPEAT_INPUT = (By.NAME, "password_confirmation")
REG_USERNAME_INPUT = (By.NAME, "name")
REG_CREATE_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(text(),'Создать аккаунт')]")

# Ошибки в регистрации
REG_EMAIL_ERROR = (By.XPATH, "//input[@name='email']/following-sibling::div[contains(@class,'error')]")
REG_PASSWORD_ERROR = (By.XPATH, "//input[@name='password']/following-sibling::div[contains(@class,'error')]")
REG_PASSWORD_REPEAT_ERROR = (By.XPATH, "//input[@name='password_confirmation']/following-sibling::div[contains(@class,'error')]")

# Поля входа
LOGIN_EMAIL_INPUT = (By.NAME, "email")
LOGIN_PASSWORD_INPUT = (By.NAME, "password")
LOGIN_BUTTON = (By.XPATH, "//button[contains(text(),'Войти')]")

# Кнопка выхода
LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(),'Выйти')]")

# Модальное окно для создания объявления (для неавторизованных)
CREATE_AD_MODAL_TITLE = (By.XPATH, "//div[contains(@class,'modal')]//h2[contains(text(),'Чтобы разместить объявление, авторизуйтесь')]")

# Форма создания объявления
AD_TITLE_INPUT = (By.NAME, "title")
AD_DESCRIPTION_INPUT = (By.NAME, "description")
AD_PRICE_INPUT = (By.NAME, "price")
AD_CATEGORY_DROPDOWN = (By.NAME, "category")
AD_CITY_DROPDOWN = (By.NAME, "city")
AD_CONDITION_RADIO_NEW = (By.XPATH, "//input[@name='condition' and @value='new']")
AD_CONDITION_RADIO_USED = (By.XPATH, "//input[@name='condition' and @value='used']")
AD_PUBLISH_BUTTON = (By.XPATH, "//button[contains(text(),'Опубликовать')]")

# Профиль пользователя и его объявления
PROFILE_BUTTON = (By.XPATH, "//a[contains(text(),'Профиль')]")
MY_ADS_BLOCK = (By.XPATH, "//div[contains(@class,'my-ads')]")
MY_ADS_TITLES = (By.XPATH, "//div[contains(@class,'my-ads')]//h3")
