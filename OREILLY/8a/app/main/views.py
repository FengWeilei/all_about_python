from flask import render_template, session, redirect, url_for, current_app
from .. import db
from ..models import User
from ..email import send_email
from . import main
from .forms import NameForm

# 注意，这里是main.route(),不是app.route（在蓝本中添加路由）
@main.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            session['known'] = False
            if current_app.config['FLASKY_ADMIN']:
                send_email(current_app.config['FLASKY_ADMIN'], 'New User',
                           'mail/new_user', user=user)
        else:
            session['known'] = True
        session['name'] = form.name.data
        return redirect(url_for('.index'))
    return render_template('index.html',
                           form=form, name=session.get('name'),
                           known=session.get('known', False))


# 然后这个url_for('.index')
# 单个文件中默认是url_for('index')
# url_for() 函数的第一个参数是路由的端点名，在程序的路由中，默认为视图函数的名字。
# 例如，在单脚本程序中，index() 视图函数的URL 可使用url_for('index') 获取。
# 在蓝本中就不一样了，Flask 会为蓝本中的全部端点加上一个命名空间，
# 这样就可以在不同的蓝本中使用相同的端点名定义视图函数，而不会产生冲突。
# 命名空间就是蓝本的名字（Blueprint 构造函数的第一个参数），
# 所以视图函数index() 注册的端点名是main.index，其URL 使用url_for('main.index') 获取。

# 同一蓝本中，省略了蓝本名main，就成了url_for('.index')