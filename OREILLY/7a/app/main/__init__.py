from flask import Blueprint   # 蓝本也可以是单个文件（将main文件夹中四个文件合并一下）

main = Blueprint('main', __name__)  # 通过实例化一个Blueprint对象来创建蓝本，
# 第一个参数为蓝本的名字，第二个参数为蓝本所在的包或模块。__name__变量就存储着当前模块的名字。

from . import views, errors  # . 表示当前路径，从这个main文件夹中导入views、errors
# 主要在末尾导入了views, errors，因为在views.py和errors.py中还要导入main(避免循环导入)