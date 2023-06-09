# ТЗ (MVP)

Написать сервис, который принимает изображения для сохранения в 
медиатеку для будущего использования.

Важные моменты:
- в БД необходимо записать следующие данные о  файле:
  - название
  - путь
  - UUID
  - тип (изображение, видео, аудио)
  - файл
  - для видео сохранить обложку(опционально)
- авторизация по токену на предъявителя, при этом авторизация может быть:
  - через отдельный эндпоинт
  - через токен с проверкой гет параметра
- описана документация и доступ во вне
- CR[UD] для медиа файла

## Extra
- если пользователь не авторизован, то:
  - при запросе изображения необходимо возвращать этот файл, эффектом блюра
  - при запросе видео, необходимо возвращать обложку видео


# Решение
# Проект по загрузке медиа файлов

Проект должен поддерживать загрузку файлов и сохранять их по определенному пути

## Стек
- fastapi
- postgresql

## Зависимости

В файле requirements.txt

Установить 

```pip install -r requirements.txt```


## Запуск

``uvicorn src.main:app --host 0.0.0.0 --port 8066 --reload --reload-dir .``

## Описание

Реализованы два эндпоинта:
- сохранение информации по файлу без загрузки файла
- возврат списка файлов
- возврат информации по одному файлу
- обрабатывает авторизацию по токену для получения файла

---
# Бизнес-требование
