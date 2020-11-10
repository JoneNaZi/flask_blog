from flask import render_template, redirect, url_for, flash
from sqlalchemy import and_
from . import profile
from .forms import LoginForm, AddForm
from models import User, Directory
from run import db


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
    directory_obj_list = Directory.query.all()
    return render_template('index.html', directory_obj_list=directory_obj_list)


@profile.route('/detail/<directory_id>')
def detail(directory_id):
    directory = Directory.query.filter(Directory.id == directory_id).first()
    return render_template('detail.html', directory=directory)


@profile.route('/add_blog', methods=['GET', 'POST'])
def add_blog():
    add_form = AddForm()
    title = add_form.title.data
    content = add_form.content.data
    if add_form.validate_on_submit():
        db.session.add(Directory(title=title, content=content))
        return redirect(url_for('profile.index'))
    return render_template('add_blog.html', form=add_form)
