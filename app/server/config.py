import os
basedir = os.path.abspath(os.path.dirname(__file__))

# db credentials
user = os.environ.get("mysql_user") or "test"
password = os.environ.get("mysql_password") or "password"
host = os.environ.get("mysql_host") or "localhost"

mysql_local_base = 'mysql+pymysql://' + user + ':' + password + '@' + host +'/'
print(mysql_local_base)
database_name = 'reBit'

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'
    SQLALCHEMY_DATABASE_URI = mysql_local_base + database_name
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    BCRYPT_LOG_ROUNDS = 13