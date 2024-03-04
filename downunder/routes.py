from flask import render_template, request, flash, redirect, url_for, jsonify
from downunder import app, db
from downunder.models import Topic, Question, User, Question
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user 
from flask_login import current_user, LoginManager
# Added flask forms having looked at the potential benefits 
# (https://flask.palletsprojects.com/en/2.3.x/patterns/wtforms/)
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


### Display urgent and latest questions as well as user info on home page ###
@app.route("/")
def home():
    """
    Navigate to home page and load latest questions
    to the main discussion area
    """
    questions = list(Question.query.order_by(Question.id).all())
    return render_template("index.html", 
    page_title="Welcome to Chat Down Under",
    user=current_user, questions=questions
    )


### TOPIC SPECIFIC ROUTES ###
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


### ADD TOPICS ###
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
        user=current_user)

### DELETE TOPICS ###
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
    


### QUESTION SPECIFIC ROUTES ###
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
        #Gather all selected topic Id's
        selected_topic_ids = request.form.getlist('question_topics')
        is_urgent = request.form.get('is_urgent') == 'on'

        new_question = Question(
                                question_title=question_title, 
                                question_body=question_body, 
                                author_id=current_user.id, 
                                is_urgent=is_urgent
                                )
        db.session.add(new_question)


        selected_topic_ids = [
            topicid for topicid in selected_topic_ids if topicid != 'new_topic'
            ]

        # Add/append each topic to the question
        for topicid in selected_topic_ids:
            topic = Topic.query.get(int(topicid))
            if topic:
                new_question.topics.append(topic)

        db.session.commit()
        flash('Your question has been added!', category='success')
        return redirect(url_for('home'))

    topics = Topic.query.all()
    return render_template(
        "submit_question.html", 
        page_title="Ask Your Question", 
        topics=topics, 
        user=current_user)

@app.route('/edit_question/<int:question_id>', methods=['GET', 'POST'])
@login_required
def edit_question(question_id):
    """
    Load edit question page and allow resubmission and editing of question
    """
    question = Question.query.get_or_404(question_id)
    #Safety measure to ensure only author can edit the question
    if current_user.id != question.author_id:
        flash('You can only edit your own questions.', category='error')
        return redirect(url_for('home'))

    topics = Topic.query.all()

    if request.method == 'POST':
        # Collect data from form
        question_title = request.form['question_title']
        question_body = request.form['question_body']
        selected_topics_ids = request.form.getlist('topics')
        # Update question data
        question.question_title = question_title
        question.question_body = question_body
        question.topics = [
            Topic.query.get(int(topicid)) for topicid in selected_topics_ids
            ]
        #commit this edit
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


### REPLY SPECIFIC ROUTES ###
@app.route('/reply')
#Only logged in users can reply to questions
@login_required
def reply():
    """
    Initiates reply textbox allocating author and question
    """
    print(reply)


### AUTHETNTICATION ROUTES ###
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
                'Password too short - your password must be at least 8 chars', 
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
#ensure users can only log out if logged in
@login_required
def logout():
    logout_user()
    flash('You have successfully logged out', category='success')
    return redirect(url_for('home'))
    