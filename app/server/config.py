import os
basedir = os.path.abspath(os.path.dirname(__file__))
mysql_local_base = 'mysql+pymysql://test:password@localhost/'
database_name = 'reBit'

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'
    SQLALCHEMY_DATABASE_URI = mysql_local_base + database_name
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    BCRYPT_LOG_ROUNDS = 13