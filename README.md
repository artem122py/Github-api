# Github-api
Test GitHub api

Этот репозиторий написан на языке python, в нём есть код который регистрируется на GitHub и выдаёт username.

**Статус:** Экспериментальный / Игрушечный проект.  
Создан для ознакомления с GitHub API. Не рекомендуется к использованию.

[![Experimental](https://img.shields.io/badge/status-experimental-red.svg)](https://github.com/ваш-username/repo)
[![For fun](https://img.shields.io/badge/purpose-for%20fun-yellow.svg)](https://github.com/ваш-username/repo)
## Установка зависимостей 
```bash pip install -r requirements.txt```

## Настройка
1. Откройте файл main.py
2. найдите строки client_id, client_secret, redirect_url.
3. Измените параметры на свой настройки.

## Запуск
```bash python main.py```


### Примерный вывод
```Follow the link https://github.com/login?***user to start authentication```
```Enter just code:```

Затем перейдите по ссылке и авторизуйтесь, а затем вас перекинет на ссылку в redirect_url и скопируй код в URL https://example.com/?code=***
и введите в программу, и затем вам напишет ваш username
