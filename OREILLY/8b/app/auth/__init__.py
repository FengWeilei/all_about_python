from flask import Blueprint   # 为用户认证，新写了一个auth蓝本。

auth = Blueprint('auth', __name__)  # 通过实例化一个Blueprint对象来创建蓝本，
# # 第一个参数为蓝本的名字，第二个参数为蓝本所在的包或模块。__name__变量就存储着当前模块的名字。

from . import views  # . 表示当前文本路径中导入路由。


# 复习一下，蓝本中创建路由，只有注册蓝本后，这些路由才会激活。
# 写好蓝本后，记得在app/__init__.py中的create_app()中注册蓝本。


# 对于不同的程序功能，我们要使用不同的蓝本，这是保持代码整齐有序的好方法。