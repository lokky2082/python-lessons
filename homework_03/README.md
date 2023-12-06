### Домашнее задание "Docker контейнер c веб-приложением"
#### Задача:
- скопируйте папку `homework_03` для этой домашки 
  (Памятка: https://github.com/OtusTeam/BasePython/tree/homeworks-new)
- обязательно используйте виртуальное окружение
- никогда не добавляйте в репозиторий своё локальное виртуальное окружение
- установите `FastAPI` и `uvicorn`
    - инструмент на ваш выбор: pip, Pipenv, poetry
- создайте веб приложение на `FastAPI`
- обязательно добавьте view со следующими свойствами 
  (данный view будет использован для проверки):
    - путь `/ping/`
    - статус ответа `200`
    - тело ответа — JSON объект `{"message": "pong"}`
- соберите зависимости для своего веб-приложения
    - инструмент на ваш выбор: requirements.txt, Pipenv, poetry
- создайте/отредактируйте Dockerfile. В нём должно быть выполнено следующее:
    - установка зависимостей
    - копирование всех модулей приложения
    - запуск вебсервера `uvicorn` c параметрами host `0.0.0.0` и port `8000`
- допишите в заголовок файла комментарий с информацией о том, как запустить этот контейнер 
  (можно готовую строчку запуска с проброшенными портами и тд)
- по желанию добавьте в приложение другие фичи (например те, что мы писали на уроке)
#### Критерии оценки:
- Dockerfile создан
- зависимости устанавливаются отдельно
- после этого копируется всё приложение
- приложение запускается
- объявлено, какой порт нужно использовать (директива EXPOSE)
- используется порт 8000
- есть комментарий с информацией о том, как запускать этот контейнер
- автоматический тест `test_homework_03` проходит
#### Как запустить контейнер:
docker build . -t app
docker run -p 8080:8000 -it app
