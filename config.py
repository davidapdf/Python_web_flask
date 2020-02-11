import os

SECRET_KEY = 'senha_super_secreta'
MYSQL_HOST = "127.0.0.1"
MYSQL_USER = "root"
MYSQL_PASSWORD = "A1s2d3f4g5"
MYSQL_DB = "jogoteca"
MYSQL_PORT = 3306
UPLOAD_PATH = f'{os.path.dirname(os.path.abspath(__file__))}/uploads'