from flask import Flask, render_template, make_response

app = Flask(__name__)

@app.route('/response')
def response():
	resp = make_response(render_template('text.txt'), 200 , {'Content-Type':'text/plain'})
	# make_response可以接受三个参数，返回值内容、HTTP状态码、返回值类型的字典
	return resp

@app.route('/xml')
def xml():
	return '<h1>this is shown as <b>XML</b> in the browser</h1>', 200, {'Content-Type':'application/xml'}
	
if __name__ == "__main__":
	app.secret_key = "For safety"
	app.run(debug=True)