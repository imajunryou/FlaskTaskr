import os

# grab the folder where this script lives
basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = "flasktaskr.db"
USERNAME = "admin"
PASSWORD = "admin"
WTF_CSRF_ENABLED = True
SECRET_KEY = 'gy|\xa6\xfa\x88}\xb4[\xcdH\xfb\xf1\xfa\xb3w<\x8a\t\xda\xb4Cep'

# define the full path for the database
DATABASE_PATH = os.path.join(basedir, DATABASE)
