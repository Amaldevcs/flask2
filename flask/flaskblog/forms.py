from flask_wtf import FlaskForm
from wtforms import SubmitField
from flaskblog.models import Sessions
class LoginForm(FlaskForm):
	submit = SubmitField('Login')


