from flask import render_template, request, url_for
from Ostrich import app
import models


@app.route('/')
def index():
    user = {'name': 'Miguel'}  # fake user
    posts = [  # fake array of posts
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template("index.html",
                           title='Home',
                           user=user,
                           posts=posts)

@app.route('/posted', methods=["GET","POST"])
def posted():
    name = request.form['name']
    location = request.form['location']
    course = request.form['course']
    shirt = request.form['shirt']
    new_post = models.User(name, location, course, shirt)
    models.db.session.add(new_post)
    models.db.session.commit()
    return render_template("index.html", name=name)