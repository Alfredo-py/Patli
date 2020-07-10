class BaseConfig(object):
    'Base configuracion'
    SECRET_KEY = 'Key'
    DEBUG = True
    TESTING = False
class ProductionConfig(BaseConfig):
    'Produccion configuracion'
    DEBUG = False
class DevelopmentConfig(BaseConfig):
    'Desarrollo configuracion'
    DEBUG = True
    TESTING = True
    SECRET_KEY = 'Desarrollo key'
    SQLALCHEMY_DATABASE_URI="mysql+pymysql://root:Agp<2018d@localhost:3306/pythonp"
