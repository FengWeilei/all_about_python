from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/',methods=["GET","POST"])
def index():
	name = None  # name 默认值为None，模板中的 if 语句不成立。

	# 用户的请求中如果HTTP方法是"POST"，并且用户提交的表单中有有 name 属性（name="name"）运行之后的代码
	if request.method == "POST" and 'name' in request.form:
		name = request.form['name']  # 将用户提交的表单中 name 字段的值赋给一个 name 变量。
	return render_template("index.html",name=name)  # 将name变量作为参数传递到index.html模板中，默认的是None, 用户输入值后存储用户输入数据。

@app.errorhandler(404) 
def page_not_found(e):
	return render_template("404.html"),404

if __name__ == '__main__':
	app.run(debug=True)