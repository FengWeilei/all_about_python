from flask import Flask
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import config

# 实例化好多对象。
bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()

# 用户登录。 
login_manager = LoginManager()  #先实例化一个对象。
login_manager.session_protection = 'strong'  # 保护等级很高。Flask-Login 会记录客户端IP地址和浏览器的用户代理信息，如果发现异动就登出用户
login_manager.login_view = 'auth.login'  #设置登录页面的端点。 auth蓝本中的login路由。

# 这里实例化app对象写在了方法中，条用create_app才会实例化一个app对象。
def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app) # 刚才实例化时没有传递参数，这里传递了app参数。
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)   # 蓝本注册后，蓝本中的路由才能使用。

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')  # 这里为蓝本中的路由加上了 /auth前缀。访问时也需要加前缀访问。

    return app  # 方法最后返回app对象。
