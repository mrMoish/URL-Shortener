# URL Shortener Service

Микросервис для сокращения ссылок, реализованный на **FastAPI**, **PostgreSQL** и **Docker**.

## Функциональность

Сервис предоставляет REST API:

* **POST /shorten** — создать короткую ссылку
* **GET /{short_id}** — редирект на оригинальную ссылку
* **GET /stats/{short_id}** — статистика переходов

---

# Стек технологий

* Python 3.11
* FastAPI
* Uvicorn
* PostgreSQL
* SQLAlchemy
* Docker / Docker Compose

---

# Структура проекта

```
project/
│
├── app/
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── database.py
│   └── crud.py
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

# Запуск проекта

## 1. Клонировать репозиторий

```bash
git clone https://github.com/yourname/url-shortener.git
cd url-shortener
```

---

## 2. Запустить через Docker

```bash
docker compose up --build
```

Будут подняты два контейнера:

* **api** — FastAPI приложение
* **db** — PostgreSQL

---

# API будет доступен

```
http://localhost:8000
```

Swagger документация:

```
http://localhost:8000/docs
```

---

# Использование API

## 1. Создать короткую ссылку

**POST**

```
/shorten
```

Body:

```json
{
  "url": "https://google.com"
}
```

Ответ:

```json
{
  "short_id": "abc123"
}
```

---

## 2. Перейти по короткой ссылке

**GET**

```
/{short_id}
```

Пример:

```
http://localhost:8000/abc123
```

Произойдет редирект на оригинальный URL.

---

## 3. Получить статистику

**GET**

```
/stats/{short_id}
```

Ответ:

```json
{
  "url": "https://google.com",
  "clicks": 5
}
```

---

# Переменные окружения

Настройки базы данных:

```
POSTGRES_USER=user
POSTGRES_PASSWORD=password
POSTGRES_DB=shortener
```

Строка подключения:

```
postgresql://user:password@db:5432/shortener
```

---

# Остановка сервиса

```bash
docker compose down
```

---

# Возможные улучшения

* Alembic миграции
* кэширование Redis
* rate limiting
* тесты pytest
* генерация уникальных short_id
* логирование

---
