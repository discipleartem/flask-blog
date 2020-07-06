from flask import Flask
from config import Configuration

# путь к файлу blueprint.py 
from posts.blueprint import posts

#переменная по умолчанию
#__name__ - это имя текущего файла (сейчас app.py)

app = Flask(__name__)
app.config.from_object(Configuration)

app.register_blueprint(posts, url_prefix='/blog')