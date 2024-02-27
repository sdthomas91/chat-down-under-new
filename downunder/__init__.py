import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
if os.path.exists("env.py"):
    import env


app= Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")

db = SQLAlchemy(app)

from downunder import routes #noqa


#Flask CLI workaround for db creation - Python3 command not 
# working as per my previous project - code found here
# https://stackoverflow.com/questions/
# 77477706/how-can-i-create-database-file-with-flask
@app.cli.command("create_db")
def create_db():
    db.create_all()
    print("Database tables created")