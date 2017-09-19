import unittest  # 使用unittest包来编写测试。
from flask import current_app
from app import create_app, db


class BasicsTestCase(unittest.TestCase):
    def setUp(self):  # 测试前运行，确保程序实例存在。
        self.app = create_app('testing')  #创建一个新程序
        self.app_context = self.app.app_context() #创建上下文
        self.app_context.push()  # 激活上下文 
        db.create_all()  # 创建一个新的数据库，以备不时之需。

    def tearDown(self): # 测试后运行。确保程序在测试配置中运行。
        db.session.remove()  #删除数据库中的session
        db.drop_all()  #删除所有数据库。
        self.app_context.pop()  #删除上下文

    def test_app_exists(self):
        self.assertFalse(current_app is None)

    def test_app_is_testing(self):
        self.assertTrue(current_app.config['TESTING'])
