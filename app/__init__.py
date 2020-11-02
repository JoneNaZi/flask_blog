from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config.from_pyfile('../config.py')
# 请求结束后自动提交数据库修改
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)

from .views import profile
app.register_blueprint(profile)
