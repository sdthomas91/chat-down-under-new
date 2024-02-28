from flask import render_template, request, flash
from downunder import app,db
from downunder.models import Topic, Question

@app.route("/")
def home():
    """
    Navigate to home page and load latest questions
    to the main discussion area
    """
    return render_template("index.html", 
    page_title="Welcome to Chat Down Under")

@app.route("/sign_up", methods=['GET', 'POST'])
def sign_up():
    """
    Creating routing for sign up process and
    data collection - peform a POST to submit new
    user details
    """
    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
    
        if len(username) < 1:
            flash('Username cannot be left blank')
        elif len(fname) < 1:
            flash('First Name cannot be left blank', category='error')
        elif len(lname) < 1:
            flash('Last Name cannot be left blank', category='error')
        elif password1 != password2:
            flash('Your passwords do not match', category='error')
        elif len(password1) < 8:
            flash('Password too short - your password must be at least 8 characters', category='error')
        else:
            #add user to database
            flash('Account Created! Please proceed to login', category='success')

    return render_template("sign_up.html", page_title="Sign Up!")

@app.route("/login", methods=['GET', 'POST'])
def login():
    """
    Allow customers to navigate to login page and 
    perform login with their details as long as 
    they exist in the db
    """
    return render_template("login.html", page_title="Log In!")