from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators

app = Flask(__name__)
bootstrap = Bootstrap(app)

class NameForm(FlaskForm):  #每一个表单类对应着一个Web表单。name、submit属性对应着表单中的字段。
	name = StringField("What's your name",[validators.required(),validators.Length(min=1,max=13)])
	submit = SubmitField('Submit')  # 第一个参数是表单字段的标签，第二个参数是验证函数，用来验证数据。

@app.route('/',methods=["GET","POST"])
def index():
	name = None
	form = NameForm()  #实例化一个NameForm表单。
	# 如果请求方法是"POST"，并且用户输入数据满足验证调价，执行之后的代码
	if request.method == "POST" and form.validate_on_submit():
		name = form.name.data  # 这个form来自用户提交的表单，name是表单中的一个属性，将name字段用户输入数据赋值给name变量。
	return render_template("index.html",name=name,form=form)  #传递了两个参数到index.html模板。

@app.errorhandler(404) 
def page_not_found(e):
	return render_template("404.html"),404

if __name__ == '__main__':
	app.secret_key = "It's a  Secret key"
	app.run(debug=True)