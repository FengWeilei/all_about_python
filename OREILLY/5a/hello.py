from flask import Flask, render_template, session

app = Flask(__name__)

@app.route('/')
def index():
	if 'count' not in session:  #刚开始，session中没有count
		session["count"] = 1  # 然后设置count = 1
	else:
		session["count"] += 1 # 每次刷新页面，count = count + 1
	return render_template('index.html',count=session["count"]) #传递count参数（一个数字）到index.html中

if __name__ =="__main__":
	app.secret_key = "For the session"
	app.run(debug=True)