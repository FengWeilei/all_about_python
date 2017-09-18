from flask import render_template
from . import main

#自定义的404和500页面。
@main.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

#注意这里使用了@main.app_errorhandler装饰器，如果使用errorhandler，只有蓝本中的错误才会触发程序。
@main.app_errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
