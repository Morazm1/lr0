# ЛР0 — рабочее место инженера

Демонстрационный сервис: **Flask + Redis** в двух контейнерах.
Flask-приложение работает от непривилегированного пользователя `appuser`
(UID/GID 1000) и считает визиты в Redis.

## Состав

| Файл | Назначение |
|------|------------|
| `app.py` | Flask-приложение: `/` — счётчик визитов, `/whoami` — пользователь процесса |
| `requirements.txt` | Зависимости Python |
| `Dockerfile` | Образ на базе `python:3.12-alpine`, создание `appuser`, `USER appuser` |
| `docker-compose.yml` | Два сервиса: `app` и `redis` |
| `.gitignore` | Исключает ключи и `.env` |
| `REPORT.md` | Отчёт |

## Запуск

    docker compose up -d --build
    docker compose ps
    curl -s localhost:5000/
    curl -s localhost:5000/whoami

## Остановка

    docker compose down
