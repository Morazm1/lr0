# ЛР0 — рабочее место инженера

Контейнер на базе alpine, запускается от непривилегированного пользователя `app` (UID/GID 1000).

## Запуск
    docker compose up -d --build
    docker compose ps
    docker compose logs app

Полный отчёт — в REPORT.md.
