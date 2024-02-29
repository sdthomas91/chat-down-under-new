from flask import render_template, request, flash, redirect, url_for
from downunder import app,db
from downunder.models import Topic, Question
from .models import User, Question
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user, LoginManager
# Added flask forms having looked at the potential benefits (https://flask.palletsprojects.com/en/2.3.x/patterns/wtforms/)
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired



@app.route("/")
def home():
    """
    Navigate to home page and load latest questions
    to the main discussion area
    """
    # questions = list(Question.query.order_by(Question.id).all())
    return render_template("index.html", 
    page_title="Welcome to Chat Down Under",
    user=current_user
    )


@app.route("/topics")
def topics():
    topics = list(Topic.query.order_by(Topic.topic_name).all())
    return render_template("topics.html", page_title="Browse by Topic", user=current_user, topics=topics)

class AddTopicForm(FlaskForm):
    topic_name = StringField('Topic Name', validators=[DataRequired()])
    submit = SubmitField('Add Topic')

@app.route("/add_topic", methods=["GET", "POST"])
@login_required  # if admin-only feature
def add_topic():
    form = AddTopicForm()
    if form.validate_on_submit():
        existing_topic = Topic.query.filter_by(topic_name=form.topic_name.data).first()
        if existing_topic is None:
            topic = Topic(topic_name=form.topic_name.data)
            db.session.add(topic)
            db.session.commit()
            flash('Topic added successfully.', 'success')
            return redirect(url_for("topics"))
        else:
            flash('Topic already exists.', 'error')
    return render_template("add_topic.html", page_title="Add a Topic", form=form, user=current_user)


@app.route('/reply')
#Only logged in users can reply to questions
@login_required
def reply():
    #Initiates reply textbox allocating author and question
    print(reply)

@app.route('/submit_question', methods=['GET', 'POST'])
@login_required
def submit_question():
    if request.method == 'POST':
        question_title = request.form.get('question_title')
        question_body = request.form.get('question_body')
        selected_topic_ids = request.form.getlist('question_topics')  # This gets all selected topic IDs
        new_topic_name = request.form.get('new_topic_name').strip()

        # Handle new topic creation
        if "new_topic" in selected_topic_ids and new_topic_name:
            new_topic = Topic(topic_name=new_topic_name)
            db.session.add(new_topic)
            db.session.flush()  # Flush to assign an ID to the new topic without committing the transaction
            selected_topic_ids.append(str(new_topic.id))  # Add new topic ID to the list

        selected_topics = Topic.query.filter(Topic.id.in_([int(tid) for tid in selected_topic_ids if tid.isdigit()])).all()

        new_question = Question(question_title=question_title, question_body=question_body, author_id=current_user.id, topics=selected_topics)
        db.session.add(new_question)
        db.session.commit()

        flash('Your question has been added!', 'success')
        return redirect(url_for('home'))

    topics = Topic.query.all()
    return render_template("submit_question.html", page_title="Ask Your Question", topics=topics, user=current_user)

@app.route("/sign_up", methods=['GET', 'POST'])
def sign_up():
    """
    Creating routing for sign up process and
    data collection - peform a POST to submit new
    user details
    """
    if request.method == 'POST':
        email = request.form.get('email').lower()
        username = request.form.get('username')
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        # Validate user email and ensure it is unique
        user = User.query.filter_by(email=email).first() 
        if user:
            flash(
                'Email already registered. Please use another',
                category='error'
            )
        
        #Validate username and ensure it is unique
        user_name = User.query.filter_by(username=username).first()
        if user_name:
            flash(
                'This username is unavaialble. Please use another',
                category='error'
            )
    
        if len(username) < 1:
            flash('Username cannot be left blank', category='error')
        elif len(fname) < 1:
            flash('First Name cannot be left blank', category='error')
        elif len(lname) < 1:
            flash('Last Name cannot be left blank', category='error')
        elif password1 != password2:
            flash('Your passwords do not match', category='error')
        elif len(password1) < 8:
            flash(
                'Password too short - your password must be at least 8 characters', 
                category='error'
            )
        else:
            #add new user to database
            new_user = User(
                email=email, 
                username=username, 
                fname=fname, 
                lname=lname, 
                password=generate_password_hash(
                    request.form.get("password1")
                )
            )
            #add user to system
            db.session.add(new_user)
            db.session.commit()
            # Success message flash
            flash(
                'Account Created! Please proceed to login', 
                category='success'
            )
            return redirect(url_for('login'))

    return render_template("sign_up.html", page_title="Sign Up!", user=current_user)

@app.route("/login", methods=['GET', 'POST'])
def login():
    """
    Allow customers to navigate to login page and 
    perform login with their details as long as 
    they exist in the db
    """
    if request.method == 'POST':
        email = request.form.get('loginEmail').lower()
        password = request.form.get('password')
        remember_me = 'remember_me' in request.form
        print(f"Attempting login with email: {email}")

        user = User.query.filter_by(email=email).first()
        if user:
            print(f"User found: {user.email}")  # Debug print
            if check_password_hash(user.password, password):
                flash('You are Logged In!', category='success')
                if remember_me:
                    login_user(user, remember=True)
                else:
                    login_user(user, remember=False)
                return redirect(url_for('home'))
            else:
                flash(
                    'Password incorrect - please try again!', 
                    category='error'
                )
        else:
            flash(
                'Invalid login attempt - email not registered', 
                category='error'
            )

    return render_template("login.html", page_title="Log In!", user=current_user)

@app.route('/logout')
#ensure users can only log out if logged in
@login_required
def logout():
    logout_user()
    flash('You have successfully logged out', category='success')
    return redirect(url_for('home'))
    