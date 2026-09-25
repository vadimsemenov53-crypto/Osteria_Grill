# 🍝 Osteria Grill

Веб-приложение ресторана **Osteria Grill**, разработанное на Django.

Проект представляет собой полнофункциональный сайт ресторана с возможностью регистрации пользователей, бронирования столиков, подтверждения бронирования по электронной почте, просмотра информации о ресторане и управления контентом через административную панель Django.

Проект разработан в рамках дипломной работы.

---

## 📌 Основные возможности

### Для посетителей

* просмотр главной страницы ресторана;
* просмотр информации о ресторане;
* просмотр услуг ресторана;
* просмотр сотрудников ресторана;
* просмотр контактной информации;
* регистрация пользователя;
* подтверждение электронной почты;
* авторизация;
* редактирование профиля;
* загрузка аватара;
* просмотр схемы расположения столиков;
* выбор столика;
* выбор даты и времени бронирования;
* указание количества гостей;
* добавление комментария к бронированию;
* проверка доступности столика;
* подтверждение бронирования по электронной почте;
* просмотр собственных бронирований;
* редактирование собственных бронирований;
* отмена собственных бронирований.

### Для администратора

Через административную панель Django доступны:

* управление пользователями;
* управление столиками;
* управление бронированиями;
* управление услугами ресторана;
* управление сотрудниками;
* управление контентом сайта;
* управление информацией о ресторане;
* просмотр заявок контактной формы.

---

## 🛠 Технологии

Проект разработан с использованием следующих технологий:

* **Python 3.12**
* **Django 6.1**
* **PostgreSQL 17**
* **Redis**
* **Gunicorn**
* **Nginx**
* **Docker**
* **Docker Compose**
* **Bootstrap**
* **HTML5**
* **CSS3**
* **JavaScript**
* **Poetry**
* **Git**

Дополнительно используются:

* `psycopg2` — подключение Django к PostgreSQL;
* `django-phonenumber-field` — работа с телефонными номерами;
* `Pillow` — обработка изображений;
* `python-dotenv` — загрузка переменных окружения;
* `redis` — взаимодействие с Redis.

---

## 🏗 Архитектура проекта

Проект построен на архитектуре Django MVT (Model — View — Template).

Основные приложения:

### `restaurant`

Отвечает за основную предметную область ресторана:

* столики;
* бронирования;
* услуги ресторана;
* сотрудники;
* контактные заявки.

### `users`

Отвечает за:

* пользовательскую модель;
* регистрацию;
* авторизацию;
* подтверждение электронной почты;
* профиль пользователя.

Используется собственная модель пользователя на основе `AbstractUser`.

### `content`

Отвечает за редактируемый контент сайта:

* главную страницу;
* страницу «О ресторане»;
* общий контент сайта;
* логотип;
* контакты;
* фоновое изображение.

---

## 📁 Структура проекта

```text
osteria-mario/
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── ...
│
├── restaurant/
├── templatetags/
│   │   └── restaurant_tags.py
│   ├── migrations/
│   ├── templates/
│   ├── admin.py
│   ├── booking_validation.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── users/
│   ├── management/
│   │   └── commands/
│   │       └── csu.py
├── templatetags/
│   │   └── user_tags.py
│   ├── migrations/
│   ├── templates/
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── content/
├── management/
│   │   └── commands/
│   │       └── start_content.py
│   ├── migrations/
│   ├── templates/
│   ├── admin.py
│   ├── context_processors.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── static/
│   ├── css/
│   ├── js/
│   └── ...
│
├── media/
│   ├── users/
│   ├── restaurant/
│   └── content/
│
├── nginx/
│   ├── Dockerfile
│   └── nginx.conf
│
├── start_fixtures.json
├── Dockerfile
├── docker-compose.yml
├── pyproject.toml
├── poetry.lock
├── manage.py
├── README.md
└── .env.sample
```

---

# 🐳 Запуск проекта через Docker

## Требования

Перед запуском необходимо установить:

* Docker;
* Docker Compose.

Проверить установку:

```bash
docker --version
docker compose version
```

---

## 🔐 Переменные окружения

Проект использует переменные окружения для хранения настроек базы данных, Redis, электронной почты и других параметров.

В корне проекта необходимо создать файл:

```text
.env
```

Пример структуры:

```env
# Секретный ключ приложения
SECRET_KEY=generate_secret_key

# Режим дебага
DEBUG=True(or_False)

# Настройки базы данный PostgreSQL
NAME=name_db
USER=example_user
PASSWORD=password
HOST=host_for_db
PORT=5432

POSTGRES_DB=name_db
POSTGRES_USER=example_user
POSTGRES_PASSWORD=password

# Настройки почты
EMAIL_HOST=smtp.yandex.ru(example)
EMAIL_PORT=465(example)
EMAIL_USE_TLS=False(or_True)
EMAIL_USE_SSL=True(or_False)
EMAIL_HOST_USER=example@yandex.ru
EMAIL_HOST_PASSWORD=password_for_apps_your_email

# Настройка кеширования
LOCATION=redis://redis:6379/1(example_for_cache)

# Ваш доверенный домен
CSRF_TRUSTED_ORIGINS=http://localhost,http://127.0.0.1
```

> Файл `.env` не должен добавляться в Git-репозиторий.

Для проекта рекомендуется использовать `.env.sample` с демонстрационными значениями без реальных секретов.

---

# 🚀 Запуск проекта

После клонирования репозитория перейти в директорию проекта:

```bash
cd osteria-mario
```

Запустить Docker Compose:

```bash
docker compose up --build
```

После запуска будут созданы и запущены следующие сервисы:

```text
web       — Django + Gunicorn
nginx     — веб-сервер
db        — PostgreSQL
redis     — Redis
```

После успешного запуска сайт доступен по адресу:

```text
http://localhost
```

---

## 🔄 Запуск в фоновом режиме

Для запуска контейнеров без вывода логов в текущий терминал:

```bash
docker compose up -d
```

Проверить состояние контейнеров:

```bash
docker compose ps
```

Посмотреть логи Django:

```bash
docker compose logs web
```

Посмотреть логи всех сервисов:

```bash
docker compose logs
```

---

# 🗄 Работа с базой данных

PostgreSQL запускается отдельным Docker-контейнером.

Django подключается к PostgreSQL через имя Docker-сервиса:

```env
DB_HOST=db
```

Это важно, поскольку внутри Docker-контейнера `localhost` указывает на сам контейнер Django, а не на PostgreSQL.

После запуска проекта необходимо применить миграции:

```bash
docker compose exec web python manage.py migrate
```

---

# 🌱 Загрузка начальных данных

Для проекта предусмотрена фикстура:

```text
start_fixtures.json
```

Она содержит стартовые данные проекта:

* контент сайта;
* информацию о ресторане;
* столики;
* услуги;
* сотрудников;
* другие необходимые начальные данные.

Пользователи и бронирования в стартовую фикстуру не включаются, чтобы не перезаписывать реальные пользовательские данные.

Для загрузки стартовых данных используется собственная management-команда:

```bash
docker compose exec web python manage.py start_content
```

Команда перед загрузкой очищает данные, относящиеся к начальному наполнению сайта, и загружает актуальную фикстуру.

---

# 👤 Создание администратора

Для создания администратора предусмотрена отдельная management-команда:

```bash
docker compose exec web python manage.py csu
```

После создания администратора можно открыть:

```text
http://localhost/admin/
```

и выполнить вход в административную панель Django.

> Учётные данные администратора не хранятся в фикстуре проекта.

---

# 👨‍💻 Работа с Django внутри Docker

Запуск Django shell:

```bash
docker compose exec web python manage.py shell
```

Создание миграций:

```bash
docker compose exec web python manage.py makemigrations
```

Применение миграций:

```bash
docker compose exec web python manage.py migrate
```

Сборка статических файлов:

```bash
docker compose exec web python manage.py collectstatic --noinput
```

Проверка проекта:

```bash
docker compose exec web python manage.py check
```

---

# 🧑‍💻 Пользовательская модель

В проекте используется собственная модель пользователя:

```python
class User(AbstractUser):
    ...
```

Вместо стандартного `username` используется электронная почта:

```python
USERNAME_FIELD = "email"
```

Email является уникальным идентификатором пользователя.

Дополнительно пользователь может хранить:

* номер телефона;
* аватар.

---

# 📧 Подтверждение электронной почты

После регистрации пользователь получает письмо со ссылкой для подтверждения электронной почты.

До подтверждения:

```text
is_active = False
```

После перехода по ссылке:

```text
is_active = True
```

Для отправки электронной почты используется SMTP-сервер, параметры которого задаются через `.env`.

---

# 🍽 Бронирование столиков

Пользователь может выбрать столик непосредственно на визуальной схеме ресторана.

При создании бронирования проверяются:

* авторизация пользователя;
* количество гостей;
* вместимость выбранного стола;
* дата бронирования;
* время бронирования;
* часы работы ресторана;
* доступность столика;
* пересечение с существующими бронированиями.

Продолжительность одного бронирования составляет:

```text
2 часа
```

Рабочее время ресторана:

```text
12:00 — 00:00
```

Последнее доступное время начала бронирования:

```text
22:00
```

При проверке занятости учитываются бронирования со статусами:

* `pending`;
* `confirmed`.

Отменённые бронирования не блокируют столик.

---

# 🔐 Ограничение доступа к бронированиям

Пользователь может работать только со своими бронированиями.

Для этого используются ограничения на уровне QuerySet и представлений Django.

Например, список бронирований фильтруется по текущему пользователю:

```python
Booking.objects.filter(user=self.request.user)
```

Также редактирование и отмена бронирования выполняются только для объекта, принадлежащего текущему пользователю.

Административная панель Django доступна только пользователям с соответствующими правами администратора.

---

# ⚡ Кеширование

Для кеширования используется Redis.

В Docker Redis доступен Django по адресу:

```text
redis://redis:6379/1
```

Кеш используется для ускорения загрузки отдельных страниц проекта.

Например, для страниц может использоваться Django `cache_page`.

Текущая продолжительность кеширования:

```text
5 минут
```

---

# 📦 Static и Media

В проекте разделены статические и пользовательские файлы.

### Static

```text
static/
```

Исходные статические файлы проекта:

* CSS;
* JavaScript;
* Bootstrap;
* другие ресурсы.

После выполнения `collectstatic` файлы собираются в:

```text
staticfiles/
```

Nginx отдаёт статические файлы напрямую.

### Media

```text
media/
```

Используется для загружаемых изображений:

* аватары пользователей;
* фотографии сотрудников;
* изображения контента;
* изображения ресторана.

---

# 🌐 Nginx и Gunicorn

В production-подобной Docker-конфигурации Django работает через Gunicorn.

Схема обработки запроса:

```text
Browser
   │
   ▼
 Nginx
   │
   ▼
Gunicorn
   │
   ▼
 Django
   │
   ├── PostgreSQL
   │
   └── Redis
```

Nginx используется как reverse proxy и сервер статических файлов.

Gunicorn используется для запуска Django-приложения.

---

# 🐳 Docker Compose

Проект состоит из четырёх основных сервисов:

```text
web
db
redis
nginx
```

### `web`

Django-приложение и Gunicorn.

При запуске выполняются:

```bash
python manage.py migrate
python manage.py collectstatic --noinput
gunicorn config.wsgi:application
```

### `db`

PostgreSQL 17.

Данные сохраняются в Docker volume:

```text
postgres_data
```

### `redis`

Redis используется для кеширования.

Данные Redis сохраняются в Docker volume:

```text
redis_data
```

### `nginx`

Принимает HTTP-запросы и передаёт их Django через Gunicorn.

Статические файлы обслуживаются непосредственно Nginx.

---

# 🧹 Остановка проекта

Остановить контейнеры:

```bash
docker compose stop
```

Остановить и удалить контейнеры:

```bash
docker compose down
```

> Команда `docker compose down` не удаляет именованные Docker volumes.

Чтобы удалить вместе с базой данных и другими volumes:

```bash
docker compose down -v
```

> Использовать `down -v` следует осторожно, поскольку это удалит данные PostgreSQL из Docker volume.

---

# 🔍 Проверка качества кода

Для форматирования используется Black:

```bash
black .
```

Для сортировки импортов:

```bash
isort .
```

Для проверки PEP 8:

```bash
flake8 .
```

Перед отправкой изменений в репозиторий рекомендуется выполнить:

```bash
black .
isort .
flake8 .
```

Также можно проверить Django:

```bash
python manage.py check
```

или внутри Docker:

```bash
docker compose exec web python manage.py check
```

---

# 📚 Git

Основная ветка проекта:

```text
main
```

Для дальнейшей разработки рекомендуется использовать отдельные ветки:

```text
develop
feature/<название-задачи>
```

Пример:

```bash
git checkout develop
git checkout -b feature/booking-history
```

После завершения задачи изменения объединяются в `develop`, а подготовленная версия переносится в `main`.

---

# 🔒 Безопасность

Секретные данные не должны храниться непосредственно в исходном коде.

В `.env` находятся:

* `SECRET_KEY`;
* пароль PostgreSQL;
* пароль SMTP;
* данные электронной почты;
* другие чувствительные параметры.

Файл `.env` должен быть добавлен в `.gitignore`.

В репозитории рекомендуется хранить только:

```text
.env.sample
```

с демонстрационными значениями.

---

# 📋 Быстрый запуск с нуля

После клонирования проекта последовательность действий:

```bash
git clone <https://github.com/vadimsemenov53-crypto/Osteria_Grill.git>
cd osteria-mario
```

Создать `.env`.

Затем:

```bash
docker compose up --build
```

Применить миграции:

```bash
docker compose exec web python manage.py migrate
```

Загрузить начальные данные:

```bash
docker compose exec web python manage.py start_content
```

Создать администратора:

```bash
docker compose exec web python manage.py csu
```

После этого открыть:

```text
http://localhost
```

Административная панель:

```text
http://localhost/admin/
```

---

## Автодеплой на удалённый сервер

Для автоматического деплоя приложения на удалённый сервер через GitHub Actions необходимо добавить следующие **Repository Secrets**:

**GitHub → Settings → Secrets and variables → Actions → New repository secret**

| Secret                    | Назначение                                           |
| ------------------------- | ---------------------------------------------------- |
| `DOCKER_HUB_ACCESS_TOKEN` | Access Token для авторизации в Docker Hub            |
| `DOCKER_HUB_USERNAME`     | Username пользователя Docker Hub                     |
| `EMAIL_HOST_PASSWORD`     | Пароль от почтового сервиса                          |
| `EMAIL_HOST_USER`         | Email пользователя для отправки писем                |
| `SERVER_IP`               | IP-адрес удалённой ВМ, на которую выполняется деплой |
| `SSH_KEY`                 | Приватный SSH-ключ для подключения к удалённой ВМ    |
| `SSH_USER`                | Пользователь для SSH-подключения к удалённой ВМ      |

### Клонирование проекта и настройка ВМ

- Создайте свою ВМ и подключитесь к ней.
- Далее используйте готовые команды для ее настройки
- Ручная настройка осуществляется один раз далее будет работать авто-деплой.

````
- sudo apt update
- sudo apt upgrade

Скрипт установки Docker ->

# Add Docker's official GPG key:
sudo apt update
sudo apt install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
sudo tee /etc/apt/sources.list.d/docker.sources <<EOF
Types: deb
URIs: https://download.docker.com/linux/ubuntu
Suites: $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}")
Components: stable
Architectures: $(dpkg --print-architecture)
Signed-By: /etc/apt/keyrings/docker.asc
EOF

sudo apt update


- Настройка файрвола ->

sudo ufw status
sudo ufw enable

-- Открываем необходимые порты ->

sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw allow 22/tcp

- Установка Git ->

sudo apt update
sudo apt install git
git --version
git clone https://github.com/vadimsemenov53-crypto/Osteria_Grill.git
````


### Настройка `.env`

На удалённой ВМ необходимо создать файл `.env` в корневой директории проекта.

Для доступа к приложению по IP-адресу удалённого сервера укажите:

```env
cd ~/Osteria_Grill
nano .env  (за основу брать .env.sample)

# URL для доступа к приложению на удалённой ВМ
SITE_URL=22.22.222.222
```

Замените `22.22.222.222` на фактический IP-адрес вашей удалённой ВМ.

### Первый пуск проект

`sudo docker-compose up -d --build`

- После данных шагов ваш проект будет доступен по публичному IP вашей ВМ.

### Запуск автодеплоя

После настройки GitHub Secrets и `.env` деплой выполняется автоматически при push в ветку `develop`.

GitHub Actions:

1. собирает Docker image приложения;
2. публикует image в Docker Hub;
3. подключается к удалённой ВМ по SSH;
4. получает актуальный код из репозитория;
5. загружает новый Docker image;
6. перезапускает приложение.

> **Важно:** `SSH_KEY` должен соответствовать публичному ключу, добавленному в `~/.ssh/authorized_keys` пользователя `SSH_USER` на удалённой ВМ.

Не добавляйте значения `DOCKER_HUB_ACCESS_TOKEN`, `SSH_KEY`, пароли и другие секреты непосредственно в репозиторий.


---

# 📝 Статус проекта

Проект реализует основные функции сайта ресторана:

* [x] Django-приложение
* [x] PostgreSQL
* [x] Redis
* [x] Docker
* [x] Docker Compose
* [x] Nginx
* [x] Gunicorn
* [x] Bootstrap
* [x] Регистрация пользователей
* [x] Авторизация
* [x] Подтверждение электронной почты
* [x] Пользовательский профиль
* [x] Бронирование столиков
* [x] Проверка доступности столиков
* [x] Редактирование бронирования
* [x] Отмена бронирования
* [x] Подтверждение бронирования по электронной почте
* [x] Административная панель
* [x] Управление контентом
* [x] Кеширование Redis
* [x] Начальные данные через фикстуры
* [x] Management-команды
* [x] PEP 8 / Black / isort / Flake8

---

# 👨‍🎓 Дипломный проект

Разработал: Vadim Semenov

Git: <https://github.com/vadimsemenov53-crypto>

Проект разработан в рамках дипломной работы.

Основная цель проекта — разработка полнофункционального веб-приложения ресторана с возможностью онлайн-бронирования столиков и административного управления данными.

Технологический стек проекта позволяет использовать приложение как локально через Docker Compose, так и подготовить его к дальнейшему развёртыванию на удалённом сервере.
