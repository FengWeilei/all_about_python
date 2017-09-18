from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)  #实例化一个bootstrap对象，在index.html中能看到效果

@app.route('/')
def index():
	name = "FengWeilei"
	return render_template("index.html",name=name)

if __name__ == '__main__':
	app.run(debug=True)