-- Вставка пользователей
INSERT INTO users ("fullName", gender, "birthDate", address)
VALUES ('Денисова Серафима Руслановна', 'мужской', '1990-01-01', 'Москва'),
       ('Прохорова Яна Вячеславовна', 'женский', '1991-02-02', 'Санкт-Петербург'),
       ('Мухина Есения Захаровна', 'мужской', '1992-03-03', 'Новосибирск'),
       ('Сизова Ясмина Дмитриевна', 'женский', '1993-04-04', 'Екатеринбург'),
       ('Анисимов Артём Фёдорович', 'мужской', '1994-05-05', 'Красноярск'),
       ('Кузнецов Артём Артёмович', 'женский', '1995-06-06', 'Омск'),
       ('Смирнов Марк Сергеевич', 'мужской', '1996-07-07', 'Тюмень'),
       ('Никифорова Варвара Тимуровна', 'женский', '1997-08-08', 'Воронеж'),
       ('Богданов Андрей Максимович', 'мужской', '1998-09-09', 'Самара'),
       ('Ларионов Михаил Даниилович', 'женский', '1999-10-10', 'Казань');

-- Вставка электронных адресов
INSERT INTO emails ("userId", "emailType", email)
VALUES ('1', 'рабочая', 'denisova@example.com'),
       ('2', 'личная', 'prokhorova@example.com'),
       ('3', 'рабочая', 'mukhina@example.com'),
       ('4', 'личная', 'sizova@example.com'),
       ('5', 'личная', 'anisimov@example.com'),
       ('6', 'рабочая', 'kuznetsov@example.com'),
       ('7', 'личная', 'smirnov@example.com'),
       ('8', 'рабочая', 'nikiforova@example.com'),
       ('9', 'личная', 'bogdanov@example.com'),
       ('10', 'рабочая', 'larionov@example.com');

-- Вставка телефонных номеров
INSERT
INTO phones ("userId", "phoneType", phone)
VALUES ('1', 'мобильный', '+79123456789'),
       ('2', 'городской', '+79234567890'),
       ('3', 'городской', '+79345678901'),
       ('4', 'мобильный', '+79456789012'),
       ('5', 'мобильный', '+79567890123'),
       ('6', 'городской', '+79678901234'),
       ('7', 'мобильный', '+79789012345'),
       ('8', 'мобильный', '+79890123456'),
       ('9', 'городской', '+79901234567'),
       ('10', 'мобильный', '+70012345678');

-- SELECT setval('users_id_seq', MAX(id))
-- FROM users;
--
-- SELECT setval('emails_id_seq', MAX(id))
-- FROM emails;
--
-- SELECT setval('phones_id_seq', MAX(id))
-- FROM phones;
