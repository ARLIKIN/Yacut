# YaCut — сервис укорачивания ссылок

## Описание

Проект YaCut — это сервис укорачивания ссылок. Его назначение — ассоциировать длинную пользовательскую ссылку с короткой, которую предлагает сам пользователь или предоставляет сервис.

Ключевые возможности сервиса:

* генерация коротких ссылок и связь их с исходными длинными ссылками,
* переадресация на исходный адрес при обращении к коротким ссылкам.

Сервис состоит из пользовательского интерфейса и REST API.

## Технологии

[![Python](https://img.shields.io/badge/Python-3.9-000000?logo=python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.0-000000?&logo=flask)](https://flask.palletsprojects.com/)
[![SQLite](https://img.shields.io/badge/SQLite-3-000000?logo=sqlite)](https://www.sqlite.org/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-1.4-000000)](https://www.sqlalchemy.org/)
[![Alembic](https://img.shields.io/badge/Alembic-1.7-000000)](https://alembic.sqlalchemy.org/)
[![WTForms](https://img.shields.io/badge/WTForms-3.0-000000)](https://wtforms.readthedocs.io/)

## Доступные эндпоинты API

* `api/id/` — POST-запрос на создание новой короткой ссылки;
* `api/id/<short_id>/` — GET-запрос на получение оригинальной ссылки по указанному короткому идентификатору.

## Локальный запуск проекта

Клонировать репозиторий и перейти в директорию проекта:

```bash
git clone https://github.com/bvsvrvb/praktikum-yacut.git
```

```bash
cd praktikum-yacut
```

Создать `.env` файл с переменными окружения:

```
FLASK_APP=yacut
FLASK_ENV=development
DATABASE_URI=sqlite:///db.sqlite3
SECRET_KEY=YOUR_SECRET_KEY
```

Cоздать и активировать виртуальное окружение:

```bash
python -m venv venv
```

```bash
source venv/Scripts/activate
```

Установить зависимости из файла requirements.txt:

```bash
python -m pip install --upgrade pip
```

```bash
pip install -r requirements.txt
```

Выполнить миграции:

```bash
flask db upgrade
```

Запустить сервис на веб-сервере разработки Flask:

```bash
flask run
```
