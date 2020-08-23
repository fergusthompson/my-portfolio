import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo


app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'my_portfolio'
app.config["MONGO_URI"] = 'mongodb+srv://Fergus:f3rgu5@myfirstcluster.y70hl.mongodb.net/my_portfolio?retryWrites=true&w=majority'


mongo = PyMongo(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/resume')
def resume():
    return render_template('resume.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/get_skills')
def get_skills():
    return render_template("skills.html", skills=mongo.db.skills.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
