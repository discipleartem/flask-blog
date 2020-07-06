from flask import Blueprint
from flask import render_template


posts = Blueprint('posts', __name__, template_folder='templates')

# потому что у нас есть url_prefix='/blog'
@posts.route('/')
def index2():
	#/app/posts/templates/posts
	return render_template('posts/index.html')