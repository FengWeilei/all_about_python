from flask import render_template
from . import auth  # 这里导入了auth蓝本，创建路由时要知道是为哪个蓝本创建的。

# 然后使用蓝本的route 修饰器定义与认证相关的路由
@auth.route('/login')
def login():
    return render_template('auth/login.html')  # 在默认的templates文件夹中创建的专属的auth文件夹。
