# -*- coding: utf-8 -*-

from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def home():
	return '<h1>HOME</h1>'

@app.route('/signin',methods=['GET'])   # GET 显示这个，和下面POST不一样
def signin_form():
	return """<form action='/signin' method='post'>
	<p><input name='username'></p>
	<p><input name='password' type='password'></p>
	<p><button type='submit'>Sign In</button></p>
	</form>
	"""

@app.route('/signin', methods=['POST'])
def signin():
	if request.form['username'] == 'FengWeilei' and request.form['password'] == 'password':
		return '<h2> You are now signed in.</h2>'
	return '<h2>Please try again</h2>'

if __name__ == '__main__':
	app.run()
