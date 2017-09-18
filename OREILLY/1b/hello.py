from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
	return """
<!DOCTYPE html>
<html>
<head>
	<title>Flask 1b</title>
</head>
<body>
	<p>hello world from HTML.</p>
</body>
</html>
"""

if __name__ == '__main__':
	app.run(debug=True)