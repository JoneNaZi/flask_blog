from flask import Blueprint, render_template, redirect, url_for, request
from models import User
profile = Blueprint('profile', __name__)


# @profile.route('/')
@profile.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        da = User.query.all()
        print(da)
        username = request.form['username']
        password = request.form['password']
        if username == 'dengzhi' and password == 'dengzhi':
            return redirect(url_for('index', username=username, password=password))
    return render_template('login.html')


@profile.route('/index')
def index():
    return render_template('index.html')