from flask import render_template, redirect, url_for, request
from . import profile
from models import User


# @profile.route('/')
@profile.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'dengzhi' and password == 'dengzhi':
            return redirect(url_for('profile.index', username=username, password=password))
    return render_template('login.html')


@profile.route('/index')
def index():
    return render_template('index.html')