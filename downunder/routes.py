from flask import render_template
from downunder import app,db


@app.route("/")
def home():
    return render_template("index.html")