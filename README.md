# Sprint_5
# UI Автотесты для учебного сервиса «Доска»

Проект содержит UI-тесты для функциональностей учебного сервиса «Доска» на сайте https://qa-desk.stand.praktikum-services.ru/

## Используемые технологии

- Python
- Selenium WebDriver
- Pytest
- Google Chrome

## Структура проекта

- `locators/` — хранение локаторов
- `tests/` — тесты по функциональностям
- `conftest.py` — фикстуры для запуска браузера
- `utils.py` — вспомогательные функции (например, генерация email)

## Запуск тестов

```bash
pytest tests/
