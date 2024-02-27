from downunder import db

class Topic(db.Model):
    #adding ID for Topic table
    id = db.Column(db.Integer, primary_key=True)

class Question(db.Modal):
    #adding ID for Question table
    id = db.Column(db.Integer, primary_key=True)
