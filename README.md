# django-chat-application
Chat application based on django :)

Привет, первым делом вам нужно скопировать репозиторий.
* Скопировать репозиторий:
```
git clone https://github.com/AktanKasymaliev/django-chat-application.git
```
* Скачать виртульное окружени:
```
pip install python3-venv 
python3 -m venv venv
Aктивация: python3 -m venv venv
```
* Установить все зависимости: 
```
pip install -r req.txt
```

* Создать файл settings.ini на уровне самого проекта, скопировать строки ниже, и подставить свои значения
```
[DATABASE]
NAME=
USER=
PASSWORD=
HOST=
PORT=

[SYSTEM]
DEBUG=
DAJNGO_KEY=""
```

* Этот проект был сделан на Postgresql, так что устанавливаем бд:
```
sudo apt-get update
sudo apt-get install python3-pip python3-dev libpq-dev postgres postgres-contrib (MacOS) / 
sudo apt-get install postgresql postgresql-contrib (Ubuntu)
sudo su - postgres(MacOS) /
sudo -u postgres psql
```
* Зайдите в Postgresql:
```
CREATE DATABASE <database name>;
CREATE USER <database user> WITH PASSWORD 'your_super_secret_password';
ALTER ROLE <database user> SET client_encoding TO 'utf8';
ALTER ROLE <database user> SET default_transaction_isolation TO 'read committed';
ALTER ROLE <database user> SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE <database name> TO '<database user>';
```
* Установите Redis или воспользуйтесь docker'ом
```
Docker variant - docker run -p 6379:6379 -d redis:5
Terminal variant - sudo apt install redis-server \
                   sudo service redis-server start
```

* Синхронизируйте django с базой данных
```
- python manage.py makemigrations
- python manage.py migrate
```

* Наконец запустите сервер: `python3 manage.py runserver`
