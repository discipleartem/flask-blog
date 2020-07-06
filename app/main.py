# from app.py импортируем переменную app
from app import app
import view
from app import db

# путь к файлу blueprint.py 
from posts.blueprint import posts


app.register_blueprint(posts, url_prefix='/blog')

# включение режима отладки напрямую:
# app.run(debug=True)

# но лучше использовать файл config.py и
# импортировать настройки 

# в app.py:
# from config import Configuration
# app.config.from_object(Configuration)

if __name__ == '__main__':
	app.run()
