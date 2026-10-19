# ЛР0. Рабочее место инженера

**Студент:** <Размариновский Даниил Михайлович>
**Группа:** <БИС-24-1>
**Дата:** 2026-10-19

## 1. Постановка задачи

Развернуть воспроизводимое окружение для приложения: Dockerfile,
docker-compose.yml, контейнер должен работать от непривилегированного
пользователя. Продемонстрировать разницу между запуском от root
и от отдельного пользователя.

## 2. Состав репозитория

| Файл | Назначение |
|------|------------|
| `Dockerfile` | Сборка образа на базе `alpine:3.20`, создание пользователя `app` (UID/GID 1000) |
| `docker-compose.yml` | Описание сервиса `app`, сборка и запуск контейнера `lr0-app` |
| `entrypoint.sh` | Точка входа: печатает `WHOAMI` и `UID_GID`, затем спит |
| `README.md` | Краткая инструкция по запуску |
| `REPORT.md` | Отчёт о выполнении работы |
| `.gitignore` | Исключает приватные ключи и `.env` из репозитория |

Образ: `lr0-app:local`. Пользователь: `app`, UID 1000, GID 1000.

## 3. Эксперимент 1 — директива USER закомментирована

В `Dockerfile` строка `USER app` закомментирована, контейнер запускается
от имени по умолчанию (root).

Вывод `docker compose ps`:

NAME      IMAGE           COMMAND                SERVICE   CREATED                  STATUS                  PORTS
lr0-app   lr0-app:local   "/app/entrypoint.sh"   app       Less than a second ago   Up Less than a second


Вывод `docker compose logs app | grep WHOAMI`:

lr0-app  | WHOAMI=root


## 4. Эксперимент 2 — директива USER раскомментирована

Строка `USER app` активна, процесс запускается от непривилегированного
пользователя.

Вывод `docker compose ps`:

NAME      IMAGE           COMMAND                SERVICE   CREATED                  STATUS                  PORTS
lr0-app   lr0-app:local   "/app/entrypoint.sh"   app       Less than a second ago   Up Less than a second


Вывод `docker compose logs app | grep WHOAMI`:

lr0-app  | WHOAMI=app


## 5. SSH-ключ

ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIJXhum7cSFXflhsgHL8Rr9FXJRXAaRR7aBPPRp2bS5Vs razmarin.2006@gmail.com

