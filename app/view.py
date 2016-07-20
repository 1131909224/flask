# -*- coding: UTF-8 -*-
from flask import Flask, request, render_template

from app.mysql_helper import select_username_password

app = Flask(__name__)


@app.route('/', methods=['GET'])
def form():
    return render_template('form.html')


@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


@app.route('/hello', methods=['GET'])
def hello():
    return 'Hello, World'


@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if not username or not password:
        return render_template('form.html', message="用户密码不能为空", username=username)
    items = select_username_password(username)
    if items:
        if password == items['password']:
            return render_template('index.html', username=username)
        else:
            return render_template('form.html', message="用户密码不匹配", username=username)
    else:
        return render_template('form.html', message="账号不存在", username=username)

if __name__ == '__main__':
    app.debug = True  # 开启调试模式
    app.run(host='0.0.0.0')  # 添加host,所有人都可以访问
