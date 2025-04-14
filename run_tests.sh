#!/bin/bash

echo "✅ Установка зависимостей"
pip install -r requirements.txt

echo "🚀 Запуск тестов с Allure"
pytest --alluredir=allure_results

echo "📊 Открытие Allure-отчёта"
allure serve allure_results