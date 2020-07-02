# from app.py импортируем переменную app
from app import app
import view

# включение режима отладки напрямую:
# app.run(debug=True)

# но лучше использовать файл config.py и
# импортировать настройки 

# в app.py:
# from config import Configuration
# app.config.from_object(Configuration)

if __name__ == '__main__':
	app.run()
