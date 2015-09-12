from flask import render_template, request, url_for
from Ostrich import app
import models


@app.route('/')
def index():
    feed=models.User.query.all()
    return render_template("index.html", name="___", feed=feed)

@app.route('/posted', methods=["GET","POST"])
def posted():
    name = request.form['name']
    location = request.form['location']
    course = request.form['course']
    shirt = request.form['shirt']
    new_post = models.User(name, location, course, shirt)
    models.db.session.add(new_post)
    models.db.session.commit()
    feed=models.User.query.all()
    idNum=new_post.id

    return render_template("index.html", name=name, feed=feed, idNum=idNum)
