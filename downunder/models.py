from downunder import db
from flask_login import UserMixin
from sqlalchemy.sql import func



# User database (Guidance on user database from Tech with Tim 
# youtube videos)
class User(db.Model, UserMixin):
    #schema for the User Database Model
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    email = db.Column(db.String(100))
    password = db.Column(db.String(255))
    fname = db.Column(db.String(50))
    lname = db.Column(db.String(50))
    is_admin = db.Column(db.Boolean, default=False, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), default=func.now())
    


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
    

    def __repr__(self):
        #__repr___ to represent itself in the form of a string
        return self.topic_name

#Association table to implement the many-to-many relationship
question_topic_association = db.Table('question_topic_association',
    db.Column(
        'question_id', 
        db.Integer, 
        db.ForeignKey('question.id'), 
        primary_key=True
        ),
    db.Column(
        'topic_id', 
        db.Integer, 
        db.ForeignKey('topic.id'), 
        primary_key=True
        )
)

class Question(db.Model):
    # schema for the Question model
    id = db.Column(db.Integer, primary_key=True)
    question_title = db.Column(db.String(50), unique=True, 
    nullable=False)
    question_body = db.Column(db.Text, nullable=False)
    is_urgent = db.Column(db.Boolean, default=False, nullable=False)
    topics = db.relationship(
                            'Topic', 
                            secondary=question_topic_association, 
                            lazy='subquery',
                            backref=db.backref('questions', lazy=True)
                            )
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    author_id = db.Column(
    db.Integer,
    db.ForeignKey('user.id'),
    nullable=False
    )

    #relationship
    author = db.relationship('User', backref='questions')

    def __repr__(self):
        return "Question #{0} - Title: {1} | Urgent: {2}".format(
            self.id, self.question_title, self.author_id
        )

#Add reply model 
class Reply(db.Model):
    """
    Schema for the Reply model to allow for active user to
    reply to a question : author_id and question_id will be 
    used to auto populate the fields of the reply
    """
    id = db.Column(db.Integer, primary_key=True)
    reply_body = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime(timezone=True), default=func.now())
    author_id = db.Column(
        db.Integer, 
        db.ForeignKey('user.id'), 
        nullable=False)
    question_id = db.Column(
        db.Integer, 
        db.ForeignKey('question.id'), 
        nullable=False
    )

    # Relationships
    author = db.relationship('User', backref='replies')
    question = db.relationship('Question', backref=db.backref('replies', lazy=True, cascade="all, delete-orphan"))

    def __repr__(self):
        return (
            f'Reply #{self.id} by User ID {self.author_id} '
            f'on Question ID {self.question_id}'
        )