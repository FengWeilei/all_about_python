from . import db
from werkzeug.security import generate_password_hash, check_password_hash

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return '<Role %r>' % self.name


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    password_hash = db.Column(db.String(128))

    @property  # @property装饰器负责把一个方法变成属性.
    def password(self):  # # 方法变成了属性，我们可以使用正常的点符号访问它。（只能写入数据，不能读取数据）
        raise AttributeError('password is not a readable attribute')   # 但是，如果我们试图将该属性设为其他值，我们会引发一个AttributeError错误。

    @password.setter  # @property本身又创建了另一个装饰器@password.setter，负责把一个setter方法变成属性赋值，于是，我们就拥有一个可控的属性操作.
    def password(self, password): # 接收用户输入密码，转换成密码散列值。
        self.password_hash = generate_password_hash(password)  # 这个函数将原始密码作为输入，以字符串形式输出密码的散列值，输出的值可保存在用户数据库中。

    def verify_password(self, password):  # 比较用户输入密码和数据库中记录的密码。
        return check_password_hash(self.password_hash, password)  # 这个函数的参数是从数据库中取回的密码散列值和用户输入的密码。返回值为True 表明密码正确。

    def __repr__(self):
        return '<User %r>' % self.username


