## Инструкция по запуску Telegram-бота:
#### 1. Клонируйте репозиторий:
    git clone https://github.com/Xyndeside/NikeShop-tg_bot.git
#### и перейдите в папку проекта:
    cd NikeShop-tg_bot
#### 2. Создайте виртуальное окружение:
    python -m venv venv
#### 3. Активируйте виртуальное окружение:
#### Для Windows:
    venv\Scripts\activate
#### Для macOS/Linux:
    source venv/bin/activate
#### 4. Установите зависимости:
    pip install -r requirements.txt
#### 5. Настройте переменные окружения:
#### Создайте файл .env на основе примера .env.example:
    cp .env.example .env
#### Откройте файл .env и заполните его своими данными:

- BOT_TOKEN=your_telegram_bot_token_here (брать через @BotFather)
- DATABASE_URL=your_database_url_here (если используется база данных)
#### 6. Запустите бота:
    python bot.py
#### 7. Готово! Бот запущен и готов к работе. Вы можете взаимодействовать с ним через Telegram.

#### PS: Для заполнения бд нужно использовать файл /app/database/seed.py