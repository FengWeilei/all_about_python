#!/usr/bin/env python
import os
from app import create_app, db
from app.models import User, Role
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand

app = create_app(os.getenv('FLASK_CONFIG') or 'default')  #如果设置了FLASK_CONFIG，使用FLASK_CONFIG。没有，就是用默认值。
manager = Manager(app) #第二章最后，有对应的内容。
migrate = Migrate(app, db) # 数据库迁移相关。


def make_shell_context():  # 为下面Python Shell定义上下文。
    return dict(app=app, db=db, User=User, Role=Role)
manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)


@manager.command  # manager.command 修饰器让自定义命令变得简单。修饰函数名就是命令名，函数的文档字符串会显示在帮助消息中。
def test():  #python manage.py test 开始测试
    """Run the unit tests."""
    import unittest  
    tests = unittest.TestLoader().discover('tests')  # 找到这个tests包
    unittest.TextTestRunner(verbosity=2).run(tests) # 开始测试，


if __name__ == '__main__':
    manager.run()  # 启动脚本。


#使用pip freeze >requirements.txt可以生成requirements.txt文件
# 安装时 pip install -r requirements.txt


# python manage.py db upgrade 可以实现数据跟踪迁移。先运行这条命令，再运行python manage.py runserver

# 单元测试时，python manage.py test