from flask import Flask, render_template, session, g
from datetime import datetime

app = Flask(__name__)


@app.before_request  # 用户请求分发给视图函数处理之前,运行这个函数
def before_request():  # 写了一个函数，下面两个视图函数都能用。
	if 'count' not in session:
		session["count"] = 1
	else:
		session["count"] += 1
	g.when = datetime.now().strftime('%H:%M:%S')
	# g 一个应用上下文，来自 werkzeug。
	# 简答介绍：An object that the application can use for temporary storage during the handling of request.
	# This variable is reset with each request.

@app.route('/')
def index():
	return render_template('index.html',count=session["count"], when=g.when)

@app.route('/same_index')
def same_index():
	return render_template('same_index.html',count=session["count"], when=g.when)

if __name__ =="__main__":
	app.secret_key = "For the session"
	app.run(debug=True)