from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
	name = "FengWeilei"
	return render_template("index.html",name=name)

@app.errorhandler(404)  # HTTP状态码，404 not found
def page_not_found(e):
	return render_template("404.html"),404

if __name__ == '__main__':
	app.run(debug=True)