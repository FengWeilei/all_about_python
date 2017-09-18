from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():   # 和教材同步，这里把hello改成了index()函数
	return render_template("index.html")  # render_template默认调用当前文件目录下的templates文件夹下的HTML模板

if __name__ == '__main__':
	app.run(debug=True)