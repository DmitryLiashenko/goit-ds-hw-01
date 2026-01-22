🏦 Debt Tracker Telegram Bot

Telegram-бот для учёта долгов и баланса группы на основе данных из Google Sheets.

🚀 Основные возможности

✅ Авторизация по Telegram username или номеру телефона
📊 Получение и отображение долгов из Google Таблиц
🕒 Показ времени последнего обновления таблицы
⚙️ Простое развёртывание на Fly.io с автоматизацией через GitHub Actions

📁 Структура проекта

bot_debts/
├── main.py                  # Точка входа, настройка и запуск бота
├── commands/                # Команды Telegram-бота
│   ├── start.py             # Команда /start — авторизация пользователя
│   └── debts.py             # Команда /debts — показ долгов и баланса
├── services/                # Логика и вспомогательные модули
│   ├── auth.py              # Авторизация пользователей
│   ├── google_sheets.py     # Работа с Google Sheets и Drive API
│   ├── get_last_modified.py # Получение времени последнего обновления таблицы
│   └── notifications.py     # Уведомления администраторам
├── requirements.txt         # Python-зависимости
├── Dockerfile               # Docker образ для деплоя
├── fly.toml                 # Конфигурация для Fly.io
├── README.md                # Этот файл
└── .env                     # Переменные окружения (не коммитится в репозиторий)

⚙️ Быстрый старт и развёртывание

Клонируйте репозиторий:
git clone https://github.com/your-username/your-repo.git
cd bot_debts

Создайте и заполните файл .env с такими переменными:
BOT_TOKEN=ваш_токен_бота_из_Telegram
SPREADSHEET_ID=ID_вашей_рабочей_таблицы
SOURCE_SPREADSHEET_ID=ID_таблицы_для_отслеживания_обновлений
CREDENTIALS_STR={"type":"service_account",...}  # JSON сервисного аккаунта Google (в виде строки)
ALLOWED_USERNAMES=user1,user2,user3            # Разрешённые Telegram username для админов
ALLOWED_PHONES=79990001122,79001234567         # Разрешённые номера телефонов (без "+")
ADMIN_CHAT_ID=ваш_telegram_id_для_уведомлений

Установите зависимости:
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

Запустите бота локально:
python main.py

Для деплоя на Fly.io (предварительно настроив flyctl):
fly launch
fly deploy

💬 Доступные команды бота

Команда	Описание
/start	Авторизация пользователя (username или телефон)
/debts	Показ долгов, кассы и времени обновления таблицы
🗝 Переменные окружения

Переменная	Описание
BOT_TOKEN	Токен вашего Telegram-бота
SPREADSHEET_ID	ID Google Таблицы с основными данными
SOURCE_SPREADSHEET_ID	ID Google Таблицы, по которой отслеживается время последнего обновления
CREDENTIALS_STR	JSON сервисного аккаунта Google в виде строки
ALLOWED_USERNAMES	Разрешённые для админ-доступа Telegram username (через запятую)
ALLOWED_PHONES	Разрешённые номера телефонов для авторизации
ADMIN_CHAT_ID	

📦 Пример содержимого .env:

BOT_TOKEN=123456789:ABCdefGHIjklMNOpqrSTUvwxYZ
SPREADSHEET_ID=1A2B3C4D5E6F7G8H9I0J
SOURCE_SPREADSHEET_ID=9I8H7G6F5E4D3C2B1A
CREDENTIALS_STR={"type":"service_account", ...}
ALLOWED_USERNAMES=admin1,admin2
ALLOWED_PHONES=79990001122,79001234567
ADMIN_CHAT_ID=123456789

🛠 Технические детали

Используется python-telegram-bot v20.x
Работа с Google Sheets через gspread и Google API
Авторизация пользователей по username или номеру телефона с проверкой списков из .env
Уведомления админам о важных событиях через отдельный Telegram-чат
Время последнего обновления таблицы определяется через Google Drive API
Легко масштабируется и настраивается под любые Google Таблицы
📜 Лицензия

MIT — свободно используйте и дорабатывайте проект!

