from flask import render_template, request, flash, redirect, url_for, jsonify
from downunder import app, db
from downunder.models import Topic, Question, User, Question, Reply
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user
from flask_login import current_user, LoginManager
# Added flask forms having looked at the potential benefits
# (https://flask.palletsprojects.com/en/2.3.x/patterns/wtforms/)
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
# Sort questions by date using SQLAlchemy desc
from sqlalchemy import desc, or_, func
from datetime import datetime


# Home Route
@app.route("/")
def home():
    """
    Navigate to home page and display urgent and latest questions as well as
    user info on home page in the main discussion area
    """
    questions = list(Question.query.order_by(desc(Question.date)).all())
    """
    Use backend to limit number of urgent blocks displayed so as to avoid
    cluttering the homepage - originally used comprehension and slcing but
    this did not yield the results I wanted. It did not place the most recent
    questions first. Instead imported sql desc as per this article
    (https://stackoverflow.com/questions/4186062/
    sqlalchemy-order-by-descending)
    """
    urgent_questions = (
        Question.query
        .filter_by(is_urgent=True)
        .order_by(desc(Question.date))
        .limit(4)
        .all()
    )
    # Add a current_date to allow for users member since to display
    current_date = datetime.now()
    """
    Used scalar method - found originally in python documentation, to
    better understand best method for returning number of questions
    but it wasn't as clear I needed it to be - found
    (https://www.tutorialspoint.com/sqlalchemy/
    sqlalchemy_orm_returning_list_and_scalars.htm) instead which helped me
    decide - found this whilst reading this article
    https://stackoverflow.com/questions/55662957/
    what-is-the-difference-between-one-and-scalar
    """
    # Add query to get question count to add to user profile
    if current_user.is_authenticated:
        user_question_count = db.session.query(
            func.count(
                Question.id
            )).filter(Question.author_id == current_user.id).scalar()

    else:
        user_question_count = None
    return render_template("index.html",
                            page_title="Welcome to Chat Down Under",
                            user=current_user,
                            questions=questions,
                            urgent_questions=urgent_questions,
                            user_question_count=user_question_count,
                            current_date=current_date
                        )


# My Questions
@app.route('/my_questions')
def my_questions():
    """
    Renders a page with the current users asked questions on for easy review
    """
    questions = list(Question.query.order_by(desc(Question.date)).all())
    return render_template(
        "my_questions.html",
        page_title="My Questions",
        user=current_user,
        questions=questions)


# About Page
@app.route("/about")
def about():
    """
    Renders about page template
    """
    return render_template(
        "about.html",
        page_title="About Chat Down Under",
        user=current_user
    )


# Topic Specific Routes
@app.route("/topics")
def topics():
    """
    Renders topics page displaying a grid of current topics
    """
    topics = list(Topic.query.order_by(Topic.topic_name).all())
    return render_template(
        "topics.html",
        page_title="Browse by Topic",
        user=current_user,
        topics=topics
        )


# Add Topics
class AddTopicForm(FlaskForm):
    topic_name = StringField('Topic Name', validators=[DataRequired()])
    submit = SubmitField('Add Topic')


@app.route("/add_topic", methods=["GET", "POST"])
@login_required  # if admin-only feature
def add_topic():
    """
    Loads form to add a new topic
    """
    form = AddTopicForm()
    if form.validate_on_submit():
        existing_topic = Topic.query.filter_by(
            topic_name=form.topic_name.data
            ).first()
        if existing_topic is None:
            topic = Topic(topic_name=form.topic_name.data)
            db.session.add(topic)
            db.session.commit()
            flash('Topic added successfully.', category='success')
            return redirect(url_for("topics"))
        else:
            flash('Topic already exists.', category='error')
    return render_template(
        "add_topic.html",
        page_title="Add a Topic",
        form=form,
        user=current_user
        )


# Delete Topics
@app.route('/delete_topic/<int:topic_id>')
@login_required
def delete_topic(topic_id):
    """
    Allows admins to delete topic ID
    Would like to implement some logic to say "if user is not admin then
    flash 'you do not have permission to delete'. However, as the buttons will
    only show to admin users it is not necessary at this time
    """
    topic = Topic.query.get_or_404(topic_id)
    db.session.delete(topic)
    db.session.commit()
    flash('Topic has successfully been deleted')
    return redirect(url_for('topics'))


# Questions Specific Routes
# Add Question
@app.route('/submit_question', methods=['GET', 'POST'])
@login_required
def submit_question():
    """
    Generates form to allow users to submit a new question
    Allows users to select from existing topics
    """
    if request.method == 'POST':
        question_title = request.form.get('question_title')
        question_body = request.form.get('question_body')
        selected_topic_ids = request.form.getlist('question_topics[]')
        is_urgent = request.form.get('is_urgent') == 'on'

        new_question = Question(
                                question_title=question_title,
                                question_body=question_body,
                                author_id=current_user.id,
                                is_urgent=is_urgent
                                )

        # Add/append each topic to the question
        for tid in selected_topic_ids:
            topic = Topic.query.get(int(tid))
            print(topic)
            if topic:
                new_question.topics.append(topic)
        print(selected_topic_ids)
        print(request.form)
        db.session.add(new_question)
        db.session.commit()
        flash('Your question has been added!', category='success')
        return redirect(url_for('home'))

    topics = Topic.query.all()
    return render_template(
        "submit_question.html",
        page_title="Ask Your Question",
        topics=topics,
        user=current_user)


# Edit Question
@app.route('/edit_question/<int:question_id>', methods=['GET', 'POST'])
@login_required
def edit_question(question_id):
    """
    Load edit question page and allow resubmission and editing of question
    """
    question = Question.query.get_or_404(question_id)
    # Safety measure to ensure only author can edit the question
    if current_user.id != question.author_id:
        flash('You can only edit your own questions.', category='error')
        return redirect(url_for('home'))

    topics = Topic.query.all()

    if request.method == 'POST':
        # Collect data from form
        question_title = request.form['question_title']
        question_body = request.form['question_body']
        selected_topics_ids = request.form.getlist('question_topics[]')
        # Update question data
        question.question_title = question_title
        question.question_body = question_body
        question.is_urgent = 'is_urgent' in request.form
        question.topics = [
            Topic.query.get(int(tid)) for tid in selected_topics_ids
            ]
        # commit this edit
        db.session.commit()
        flash('Question updated successfully!', category='success')
        return redirect(url_for('home', question_id=question.id))

    return render_template(
                        'edit_question.html',
                        question_id=question.id,
                        page_title="Edit Question",
                        question=question,
                        topics=topics,
                        user=current_user
    )


# Delete Question
@app.route('/delete_question/<int:question_id>')
@login_required
def delete_question(question_id):
    """
    Allows users to delete  their own quetions
    """
    question = Question.query.get_or_404(question_id)
    if current_user.id != question.author_id:
        flash('You can only delete your own questions.', category='error')
        return redirect(url_for('home'))
    db.session.delete(question)
    db.session.commit()
    flash('Question has successfully been deleted')
    return redirect(url_for('home'))


# Reply Specific Routes
# Submit Reply
@app.route('/submit_reply/<int:question_id>', methods=['POST'])
# Only logged in users can reply to questions
@login_required
def submit_reply(question_id):
    """
    Submits reply and associates it with the question for display
    """
    reply_body = request.form.get('reply_body')
    if reply_body:
        reply = Reply(
            reply_body=reply_body,
            question_id=question_id,
            author_id=current_user.id
        )
        db.session.add(reply)
        db.session.commit()
        flash('Your reply has been posted.', category='success')
    else:
        flash('Reply cannot be empty.', category='error')

    return redirect(url_for('home'))


# View Full Thread
@app.route('/view_thread/<int:question_id>')
@login_required
def view_thread(question_id):
    question = Question.query.get_or_404(question_id)
    return render_template(
        'view_thread.html',
        question=question,
        user=current_user
    )


# Search Routes
@app.route('/search_results', methods=['GET', 'POST'])
def search_results():
    """
    Loads a search results page using the input from the search bar :
    imported or_ from sqlalchemy - found more on operators here
    (https://docs.sqlalchemy.org/en/20/core/operators.html)
    Needed a way to combine multiple search terms in one function and having
    read through a number of articles this
    https://stackoverflow.com/questions/7942547/using-or-in-sqlalchemy came up
    with the best solution
    """
    search_term = request.args.get('search_term')
    if search_term:
        questions = Question.query.join(Question.topics).filter(
            or_(
                Question.question_title.ilike(f'%{search_term}%'),
                Question.question_body.ilike(f'%{search_term}%'),
                Topic.topic_name.ilike(f'%{search_term}%')
            )
        ).distinct().all()
    else:
        questions = []
    return render_template(
        'search_results.html',
        questions=questions,
        search_term=search_term,
        user=current_user)


# Auth Routes
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

        # Validate username and ensure it is unique
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
                'Password too short - your password must be at least 8 chars',
                category='error'
            )
        else:
            # add new user to database
            new_user = User(
                email=email,
                username=username,
                fname=fname,
                lname=lname,
                password=generate_password_hash(
                    request.form.get("password1")
                )
            )
            # add user to system
            db.session.add(new_user)
            db.session.commit()
            # Success message flash
            flash(
                'Account Created! Please proceed to login',
                category='success'
            )
            return redirect(url_for('login'))

    return render_template(
        "sign_up.html",
        page_title="Sign Up!",
        user=current_user
        )


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

    return render_template(
        "login.html",
        page_title="Log In!",
        user=current_user)


@app.route('/logout')
# ensure users can only log out if logged in
@login_required
def logout():
    logout_user()
    flash('You have successfully logged out', category='success')
    return redirect(url_for('home'))
