from flask import render_template
from downunder import app,db
from downunder.models import Topic, Question

@app.route("/")
def home():
    return render_template("index.html")