from downunder import db
from flask_login import UserMixin
from sqlalchemy.sql import func



# User database (Guidance on user database from Tech with Tim 
# youtube videos)
class User(db.Model, UserMixin):
    #schema for the User Database Model
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(50))
    fname = db.Column(db.String(50))
    lname = db.Column(db.String(50))
    questions = db.relationship('Question')

# Following models have been adapted from a previous project of mine 
# (https://github.com/sdthomas91/python-project-1/tree/main/taskmanager), 
# though adapted for this setup.
# Removed cascade deletion as I intend to allow questions to be tagged 
# with multiple topics. Cascade deletion runs risk of causing 
# Questions to be unnecessarily deleted in the event of a topic removal

class Topic(db.Model):
    # schema for the Topic model
    id = db.Column(db.Integer, primary_key=True)
    topic_name = db.Column(db.String(50), unique=True, nullable=False)
    #note, no cascade deletion
    questions = db.relationship("Question", backref="category", lazy=True)

    def __repr__(self):
        #__repr___ to represent itself in the form of a string
        return self.topic_name


class Question(db.Model):
    # schema for the Question model
    id = db.Column(db.Integer, primary_key=True)
    question_title = db.Column(db.String(50), unique=True, 
    nullable=False)
    question_body = db.Column(db.Text, nullable=False)
    is_urgent = db.Column(db.Boolean, default=False, nullable=False)
    topic_id = db.Column(db.Integer, db.ForeignKey("topic.id"), 
    nullable=False)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    author = db.Column(db.Integer, db.ForeignKey('user.username'))


    def __repr__(self):
        return "Question #{0} - Title: {1} | Urgent: {2}".format(
            self.id, self.question_title, self.is_urgent
        )