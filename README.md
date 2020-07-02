# flask-blog

`This is code`
    
```
This too
```

```css
#button {
    border: none;
}
```

> Quoted text.

-----------------------------------------------------------
Устанавливаем и настраиваем базу данных 

`sudo apt install mysql-server` <br/>
password for root (DB): 1

-u = user, -p = password <br/>
`mysql -u root -p`

-----------------------------------------------------------

if you have problem with login as root or change mysql root password
look at `Fix mysql root password` https://github.com/discipleartem/scripts

-----------------------------------------------------------

`show databases;`

```
set utf8 - кодировка БД 
collate - способ сравнивания 
...unicode_ci регистро-независимый поиск
flask-blog некорректное имя
```

`create database flask_blog character set utf8 collate utf8_unicode_ci;`

выход из консоли mysql <br/>
`exit;`

-----------------------------------------------------------

Установка виртуального окружения <br/>
`virtualenv --python=python3.8 venv` - в Ubuntu 20.04 по умолчанию установлен python 3.8

для установки `sudo apt install python3-virtualenv`

активация <br/>
`source venv/bin/activate`

деактивация <br/>
`deactivate`

проверка установленых пакетов \ библиотек <br/>
`pip freeze`


cохранение зависимостей как `bundle` в ruby <br/>
pip freeze > requirements.txt (лучше не использовать ибо тянет глобальные зависимости)<br/>
`pip freeze --local > requirements.txt`

Загрузка зависимостей как bundle install в ruby<br/>
`pip install -r requirements.txt`

-----------------------------------------------------------

Lesson 3

.../flask/app/
`touch {config,app,main,view}.py`
`pip install flask`


repl and virtualenv
не забыть установить `SublimeREPL` через `Package Control`
https://www.youtube.com/watch?v=v3PIblL_Kq8

-----------------------------------------------------------

lesson 4

https://youtu.be/oixGHKxv4y0?t=3
