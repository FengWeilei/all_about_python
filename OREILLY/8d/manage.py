#!/usr/bin/env python
import os
from app import create_app, db
from app.models import User, Role
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand

# 创建app对象。如果定义了环境变量，使用定义的值。否则，使用默认值（DevelopmentConfig）
app = create_app(os.getenv('FLASK_CONFIG') or 'default')   # README.md ~ 1
manager = Manager(app)  # 实例化manage对象，等下添加两条命令，在命令行中运行 python manage.py shell 或者 python manage.py db ...
migrate = Migrate(app, db)


def make_shell_context():   # 创建上下文，供下面的 shell 使用。
    return dict(app=app, db=db, User=User, Role=Role)   # 字典形式。
manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)


@manager.command   # manager.command 修饰器让自定义命令变得简单。修饰函数名就是命令名，函数的文档字符串会显示在帮助消息中。
def test():  # #python manage.py test 开始测试
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')  #  找到这个tests包
    unittest.TextTestRunner(verbosity=2).run(tests)  #  开始测试


if __name__ == '__main__':
    manager.run()


# 使用pip freeze >requirements.txt可以生成requirements.txt文件
# 安装时 pip install -r requirements.txt


# python manage.py db upgrade 可以实现数据跟踪迁移。先运行这条命令，再运行python manage.py runserver

# 单元测试时，python manage.py test