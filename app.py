from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'dengzhi' and password == 'dengzhi':
            return redirect(url_for('index', username=username, password=password))
    return render_template('login.html')


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
