import pymysql
pymysql.install_as_MySQLdb()

from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://{username}:{password}@{host.com}:{port}/{dbname}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

@app.route('/')
def hello():
    return 'My First API !!'