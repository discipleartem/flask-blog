from flask import Flask

from config import Configuration

from flask_sqlalchemy import SQLAlchemy


#переменная по умолчанию
#__name__ - это имя текущего файла (сейчас app.py)

app = Flask(__name__)
app.config.from_object(Configuration)


db = SQLAlchemy(app)