import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
if os.path.exists("env.py"):
    import env
import click
from flask.cli import with_appcontext

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

if os.environ.get("DEVELOPMENT") == "True":
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")  # local
else:
    uri = os.environ.get("DB_URL")
    if uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)
    app.config["SQLALCHEMY_DATABASE_URI"] = uri  # heroku

db = SQLAlchemy(app)

from downunder import routes  # noqa


login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    from downunder.models import User
    return User.query.get(int(user_id))



@app.cli.command("create_db")
def create_db():
    """
    Flask CLI workaround for db creation
    """
    """
    python3 command not
    working as per my previous project - code found here
    https://stackoverflow.com/questions/
    77477706/how-can-i-create-database-file-with-flask
    """
    # (https://docs.sqlalchemy.org/en/20/core/metadata.html)
    # Use drop_all() during development to ensure tables are purged and updated
    db.drop_all()
    db.create_all()
    print("Database tables created")


@app.cli.command("make-admin")
@click.argument("username")
@with_appcontext
def make_admin(username):
    from yourapp.models import User
    user = User.query.filter_by(username=username).first()
    if user:
        user.is_admin = True
        db.session.commit()
        print(f"{username} has been granted admin rights.")
    else:
        print("User not found.")