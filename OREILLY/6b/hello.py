from flask import Flask, render_template, request, url_for, redirect
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, validators
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\\Users\\Administrator\\Desktop\\OREILLY\\6b\\data.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
lm = LoginManager(app)
lm.login_view = 'login'

class LoginForm(FlaskForm):
	username = StringField("Username",[validators.required(),validators.Length(min=1,max=13)])
	password = PasswordField('Password', [validators.required()])
	remember_me = BooleanField("Remember me")
	submit = SubmitField('Submit')


class User(db.Model):
	__tablename__ = "users"
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(16), index=True, unique=True)
	password_hash = db.Column(db.String(30))

	def set_passworld(self, password):
		self.password_hash = generate_password_hash(password)

	def verify_password(self, password):
		return check_password_hash(self.password_hash, password)

	@staticmethod
	def register(username, password):
		user = User(username=username)
		user.set_passworld(password)
		db.session.add(user)
		db.session.commit()
		return user		

	def __repr__(self): 
		return '<User {0}>'.format(self.name)

@lm.user_loader
def load_user(id):
	return User.query.get(int(id))

@app.route('/',methods=["GET","POST"])
def index():
	
	return render_template("index.html")

@app.route('/login',methods=['GET','POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()
		if user is None or not user.verify_password(form.password.data):
			return redirect(request.args.get('next') or url_for('index'))
		login_user(user, form.remember_me.data)
	return render_template('login.html',form=form)



@app.errorhandler(404) 
def page_not_found(e):
	return render_template("404.html"),404

if __name__ == '__main__':
	db.create_all()
	app.secret_key = "It's a  Secret key"
	app.run(debug=True)