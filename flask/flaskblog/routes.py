from flask import render_template, url_for, flash, redirect, request
from flaskblog import app, db
from flaskblog.forms import LoginForm
from flaskblog.models import Sessions
from time import time
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





