from downunder import db

# Models have been adapted from a previous project of mine 
# (https://github.com/sdthomas91/python-project-1/tree/main/taskmanager), 
# though adapted for this setup.
# Removed cascade deletion as I intend to allow questions to be tagged with
# multiple topics. Cascade deletion runs risk of causing Questions to be 
# unnecessarily deleted in the event of a topic removal

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

    def __repr__(self):
        return "Question #{0} - Title: {1} | Urgent: {2}".format(
            self.id, self.question_title, self.is_urgent
        )