from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
	user = {'nickname': 'Miguel'}
	return render_template('index.html', title='home', user=user, font_url='https://fonts.googleapis.com/css?family=Roboto')