class BaseConfig(object):
	DEBUG = False
	SECRET_KEY = "my precious"
	SQLALCHEMY_DATABASE_URI = 'sqlite:///shop.db'

class DevelopmentConfig(BaseConfig):
	DEBUG = True

class ProductionConfig(BaseConfig):
	DEBUG = False