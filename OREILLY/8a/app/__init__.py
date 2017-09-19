from flask import Flask
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from config import config

bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()


def create_app(config_name):  #接收一个参数，程序的配置名，如 DevelopmentConfig。然后根据不同的开发需求，创建不同的实例。
    app = Flask(__name__)
    app.config.from_object(config[config_name])  # 从DevelopmentConfig(Config)类中配置了这些基本属性。
    config[config_name].init_app(app)  # 直接使用了init_app(app)方法

    bootstrap.init_app(app)  #这儿init_app(app)方法为空，等于只是传递了app参数。等于bootstrap=Bootstrap(app)。
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)

    from .main import main as main_blueprint    #配置好程序后，没有直接定义路由，在蓝本中定义了路由，
    app.register_blueprint(main_blueprint)  #在蓝本中定义的路由处于休眠状态，直到蓝本注册到程序上后，路由才真正成为程序的一部分。

    return app  #最后，返回app实例

