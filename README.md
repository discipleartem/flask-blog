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

`sudo apt install mysql-server`
password for root (DB): 1

-u = user, -p = password
`mysql -u root -p`


`show databases;`

set utf8 - кодировка БД 
collate - способ сравнивания 
> ...unicode_ci регистро-независимый поиск

> flask-blog некорректное имя 
`create database flask_blog character set utf8 collate utf8_unicode_ci;`

выход из консоли mysql
`exit;`

-----------------------------------------------------------

Установка виртуального окружения 
`virtualenv --python=python3.7 venv`

активация
`source venv/bin/activate`

> (venv) username@comp-name:/folder/flask-blog


деактивация
`deactivate`

проверка установленых пакетов \ библиотек 
`pip freeze`


cохранение зависимостей как `bundle` в ruby
    pip freeze > requirements.txt (лучше не использовать ибо тянет глобальные зависимости)
    `pip freeze --local > requirements.txt`

Загрузка зависимостей как bundle install в ruby
    `pip install -r requirements.txt`

-----------------------------------------------------------


lesson 3

https://youtu.be/y1edhgne48g