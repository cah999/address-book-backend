# 📖 Address Book API

## 📝 Описание проекта

Этот проект представляет собой REST API для работы с записной книжкой. API позволяет создавать, просматривать,
редактировать и удалять записи.

Подробная документация по API доступна по
адресу: http://localhost:8000/docs

## 🚀 Запуск проекта

### Запуск контейнера

```bash
docker-compose up -d --build
```

### Запуск миграций используя alembic

```bash
docker-compose exec web alembic upgrade head
```

## 📚 Краткое описание API

### Users

#### Создание пользователя

`POST api/users`

#### Получение списка пользователей

`GET api/users`

#### Получение полной информации о пользователе

`GET api/users/{user_id}`

#### Редактирование пользователя

`PUT api/users/{user_id}`
`PATCH api/users/{user_id}`

#### Удаление пользователя

`DELETE api/users/{user_id}`

### Phones

#### Создание телефона пользователя

`POST api/phones/{user_id}/new`

#### Получение списка телефонов пользователя

`GET api/phones/{user_id}`

#### Редактирование телефона

`PUT api/phones/{phone_id}`
`PATCH api/phones/{phone_id}`

#### Удаление телефона

`DELETE api/phones/{phone_id}`

### Emails

#### Создание email пользователя

`POST api/emails/{user_id}/new`

#### Получение списка email пользователя

`GET api/emails/{user_id}`

#### Редактирование email

`PUT api/emails/{email_id}`
`PATCH api/emails/{email_id}`

#### Удаление email

`DELETE api/emails/{email_id}`