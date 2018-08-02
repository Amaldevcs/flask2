from flask import Flask,render_template,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import  SubmitField
#from db import db
from time import time
app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
class Sessions(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	times = db.Column(db.Float, nullable=False, default=time)
	def __repr__(self):
		return "{}".format(self.times)



class LoginForm(FlaskForm):
	submit = SubmitField('Login')


#@app.route("/")

@app.route("/home",methods=['GET', 'POST'])
def home():
	form = LoginForm()
	if form.validate_on_submit():
		return redirect(url_for('login'))
	return render_template('login.html',title='Login',form=form)
@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/back")
def back():
    return render_template('back.html', title='Back')
@app.route("/")
@app.route("/login")
def login():
	user1 = Sessions.query.first()
	if user1:
		timea=user1.times+600
		timeb=time()
		print timea
		print timeb
		if timeb >= timea:
			db.drop_all()
			db.create_all()
			return redirect(url_for('home'))
		else:
			return redirect(url_for('back'))
	else:
			return redirect(url_for('session'))


        
@app.route("/session")
def session():
	ses=Sessions(times=time())
	db.session.add(ses)
	db.session.commit()
	print ses.times
	return render_template('account.html', title='Account')









if __name__ == '__main__':
    app.run(debug = True)




