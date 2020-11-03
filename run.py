from flask import Flask

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='app/templates', static_folder='app/static')


app.config.from_pyfile('config.py')
# 请求结束后自动提交数据库修改
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)

from app import profile
app.register_blueprint(profile)

if __name__ == '__main__':
    app.run()
