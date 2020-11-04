from flask import render_template, redirect, url_for, flash
from sqlalchemy import and_
from . import profile
from .forms import LoginForm
from models import User, Directory


# @profile.route('/')
@profile.route('/login', methods=['GET', 'POST'])
def login():
    loginform = LoginForm()
    if loginform.validate_on_submit():
        username = loginform.username.data
        password = loginform.password.data
        user = User.query.filter(and_(User.username == username, User.password == password)).first()
        if user is not None:
            return redirect(url_for('profile.index'))
        else:
            flash("用户名或密码不存在")
            return redirect(url_for('profile.login'))
    return render_template('login.html', form=loginform)


@profile.route('/index')
def index():
    title = User.query.filter_by().all()
    return render_template('index.html')