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

cd .../flask/app/ <br/>
`touch {config,app,main,view}.py` <br/>
`pip install flask` <br/>


repl and virtualenv<br/>
не забыть установить `SublimeREPL` через `Package Control`<br/>
https://www.youtube.com/watch?v=v3PIblL_Kq8<br/>

-----------------------------------------------------------

lesson 4

https://youtu.be/oixGHKxv4y0?t=3

используйте Bootstrap v. 3.3.*

https://getbootstrap.com/docs/3.3/getting-started/

Первоначальный шаблон

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
	<title>Document</title>
</head>
<body>

	<nav class="navbar navbar-inverse">
		<div class="container-fluid">
			<div class="navbar-header">
				<button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
					<span class="sr-only">Toggle navigation</span>
					<span class="icon-bar"></span>
					<span class="icon-bar"></span>
					<span class="icon-bar"></span>
				</button>
				<a class="navbar-brand" href="#">Brand</a>
			</div> <!-- navbar-header -->
			<div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
				<ul class="nav navbar-nav">
					<li class="active"><a href="#">Link <span class="sr-only">(current)</span></a></li>
					<li><a href="#">Link</a></li>
				</ul>

				<from class="navbar-form navbar-left">
					<div class="form-group">
						<input type="text" class="form-control" placeholder="Search">
					</div> <!-- form-group -->
					<button type="submit" class="btn btn-default">Submit</button>
				</from>

				<ul class="nav navbar-nav navbar-right">
					<li><a href="#">Link</a></li>
				</ul>
			</div> <!-- collapse navbar-collapse -->
		</div> <!-- container-fluid -->
	</nav>

	<div class="container">
		<div class="row">
			<h2>Hello, {{ template_name }}</h2>
		</div>
	</div>

</body>
</html>
```

-----------------------------------------------------------

lesson 5
https://youtu.be/Hkiy_eSvzIk