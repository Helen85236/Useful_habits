# Project «Useful_habits»

## Description

This project was inspired by the book "Atomic Habits" written by James Clear.
The main idea of the book is to obtain good habits and removing bad ones
through system. The Tracker webapp is realised via Django REST Framework. The
CORS has been set for the project and API documentation is available.


### Habit Constraints

There are several constraints during habit creation and modification:

1. Period or frequency - how often a habit should occur. The period should not
   exceed 7 days
2. Execution time of habit should not exceed 120 seconds
3. User is allowed to create a pleasant habit. This type of habit is result of
   completing another habit. This habit should not have any award or associated
   habit.
4. Habit can have an award or associated habit but not **both**.
5. Only pleasant habit can be used as associated.

Create database and make migrations:

```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

Run Django server:

```bash
python3 manage.py runserver
```
```
## Docker
- для начала создайте отдельный файл `.env.docker` и пропишите там свои настройки. Смотрите шаблон `.env.sample`:

### Сборка образа и запуск в фоне после успешной сборки
```
docker-compose up -d —build
```
- для остановки
```
docker-compose down