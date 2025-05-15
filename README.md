# Yatube API

## Описание
Yatube API — это API для социальной сети Yatube, где пользователи могут публиковать посты, оставлять комментарии и подписываться на других пользователей. Этот проект предоставляет удобный интерфейс для взаимодействия с функционалом Yatube через REST API.

## Установка
1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/<ваш-репозиторий>/yatube_api.git
    ```
2. Перейдите в директорию проекта:
   ```bash
   cd yatube_api
   ```
3. Создайте и активируйте виртуальное окружение:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Для Windows: venv\Scripts\activate
    ```
4. Установите зависимости:
    ```bash
   pip install -r requirements.txt
   ```
5. Примените миграции:
   ```bash
    python manage.py migrate
    ```
6. Запустите сервер:
    ```bash
   python manage.py runserver
   ```

## Примеры запросов к API
### Получение списка постов
#### Запрос:
```GET /api/v1/posts/```
#### Ответ:
```json
[
    {
        "id": 1,
        "author": "user1",
        "text": "Первый пост",
        "pub_date": "2023-01-01T12:00:00Z"
    },
    {
        "id": 2,
        "author": "user2",
        "text": "Второй пост",
        "pub_date": "2023-01-02T12:00:00Z"
    }
]
```

### Создание комментария
#### Запрос:
```POST /api/v1/posts/1/comments/```
```json
{
    "text": "Отличный пост!"
}
```
#### Ответ:
```json
{
    "id": 1,
    "post": 1,
    "author": "user1",
    "text": "Отличный пост!",
    "created": "2023-01-01T12:00:00Z"
}
```
