from flask import Blueprint

auth = Blueprint('auth', __name__)  # 实例化一个Blueprint对象来创建蓝本。第一个参数为蓝本名，第二个参数为当前文本路径。

from . import views
