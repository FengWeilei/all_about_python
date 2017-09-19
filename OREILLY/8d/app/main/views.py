from flask import render_template
from . import main

# 这个路由，方便用户登录后重定向到达。
@main.route('/')
def index():
    return render_template('index.html')
