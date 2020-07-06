class Configuration(object):
	DEBUG = True
	#сначала указываем тип БД, потом драйвер БД
	# имя пользователя и пароль " root:1 "
	# имя БД " flask_blog "
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	# SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:1@localhost/flask_blog'
	SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:1@localhost/flask_blog?auth_plugin=mysql_native_password'
