from flask import Flask, render_template

app = Flask(__name__)

@app.route('/index')
def index():
	name = "FengWeilei"  # name 变量，存储着一个字符串
	return render_template("index.html",name=name)  # 第一个name是要传递给index.html模板的参数，第二个name是上面的变量

if __name__ == '__main__':
	app.run(debug=True)