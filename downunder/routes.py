from flask import render_template
from downunder import app,db
from downunder.models import Topic, Question

@app.route("/")
def home():
    return render_template("index.html", page_title="Welcome to Chat Down Under")

@app.route("/sign_up")
def sign_up():
    return render_template("sign_up.html", page_title="Sign Up!")