from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField, ValidationError
import os

app = Flask(__name__)
bootstrap = Bootstrap(app)

class UploadForm():
	image_file = FileField('Image file')
	submit = SubmitField("Submit")

	def validate_image_file(self, field):
		if field.data.filename[-4:].lower() != '.jpg':
			raise ValidationError("Invalid file extension")

@app.route('/',methods=["GET","POST"])
def index():
	image = None
	form = UploadForm()
	if request.method == "POST" and form.validate_on_submit():
		image = 'uploads/' + form.image_file.data.filename
		form.image_file.data.save(os.path.join(app.static_folder, image))
	return render_template("index.html",image=image,form=form)

@app.errorhandler(404) 
def page_not_found(e):
	return render_template("404.html"),404

if __name__ == '__main__':
	app.secret_key = "It's a  Secret key"
	app.run(debug=True)