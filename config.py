import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config:	
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'hjjcy 2018 ip_register'
	SQLALCHEMY_TRACK_MODIFICATIONS = False	
		
class DevelopmentConfig(Config):
	SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
		'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')
		
class TestingConfig(Config):
	SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
		'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')		
		
config = {
	'development' : DevelopmentConfig,
	'testing' : TestingConfig
}		
		
		
		
		
		
		
		
		
		
		
		
