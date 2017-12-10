# -*- coding: utf-8 -*-

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def home():
	return render_template('home.html')

@app.route('/signin',methods=['GET'])   # GET 显示这个，和下面POST不一样
def signin_form():
	return render_template('signin_form.html')

@app.route('/signin', methods=['POST'])
def signin():
	username = request.form['username']
	password = request.form['password']
	if request.form['username'] == 'FengWeilei' and request.form['password'] == 'password':
		return render_template('signin.html', username=username)
	return render_template('signin_form.html', message='Please try again', username=username)

if __name__ == '__main__':
	app.run(debug=True)
