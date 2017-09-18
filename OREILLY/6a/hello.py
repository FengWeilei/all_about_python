from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
# 这里设置的是SQLite数据库（文件）的绝对路径。
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\\Users\\Administrator\\Desktop\\OREILLY\\6a\\data.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True   # 运行时根据命令行提示设置的。
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)  #使用SQLAlchemy包装一下，实例化一个db对象，时候使用db对象创建一个关系表，就能存储、查询数据了。

class NameForm(FlaskForm):
	name = StringField("What's your name",[validators.required(),validators.Length(min=1,max=13)])
	submit = SubmitField('Submit')

#每一个关系表对应着一个类，类中的属性对应着表中的字段。
class User(db.Model):
	__tablename__ = "users"
	id = db.Column(db.Integer, primary_key=True) #设置的表的第一列为id，同时设置为主键，能唯一确定一行元素。
	name = db.Column(db.String(16), index=True, unique=True)  #表中的另一列记录着名字信息。

	def __repr__(self):  #这个方法很多类中都会有，这里可以用来输出表的名字。
		return '<User {0}>'.format(self.name)

@app.route('/',methods=["GET","POST"])
def index():
	name = None  #刚开始不会显示 HELLO ，"Name"
	new = False  # 对应着index.html模板中的 Happy to see you again(数据库中有了名字后)
	form = NameForm()
	if request.method == "POST" and form.validate_on_submit():
		name = form.name.data  #将用户输入的名字存储在name变量中。
		form.name.data = ''
		# 如果数据库中的users表中差不到用户输入的名字，进行之后的操作（将名字写入数据库）
		if User.query.filter_by(name=name).first() is None:
			db.session.add(User(name=name))
			db.session.commit()
			new = True # 默认的new=False，这里改成了True,即用户第一次输入名字，会显示 pleased to meet you
	return render_template("index.html", name=name, form=form, new=new)

@app.errorhandler(404) 
def page_not_found(e):
	return render_template("404.html"),404

if __name__ == '__main__':
	app.secret_key = "It's a  Secret key"
	app.run(debug=True)