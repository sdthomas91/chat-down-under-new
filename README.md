
# Chat Down Under - A Discussion Forum for all things Australia Migration

## Milestone Project 3 - Backend Development

<h2 align="center"><img src="downunder/static/images/CDU-mockup.jpg"></h2>


* Chat Down Under is a forum website which allows users to submit their own questions, as well as view and reply to those submitted by other users going through the experience. There is the option to browse topics to allow users to easily find questions or answers. Utilising Bootstrap the site is responsive and allows for easy navigation maximising UI and UX.

* This is my Milestone Project 3 submission for Code Institute's Diploma in Web Application Development course. My website uses a relational Database powered by Flask, SQLAlchemy and PostgreSQL. The site features full CRUD functionality and is built using additional technologies that I have learnt including HTML, CSS, JavaScript and Python.

## Live Project

[View the live project here.](https://chat-down-under-6866155ac589.herokuapp.com/)

## Repository

[Find the project repository here.](https://github.com/sdthomas91/chat-down-under-new)

# Table of Contents

## Contents
   - [User experience](#user-experience)
      * [User Stories](#user-stories)
         + [First-time User](#first-time-user)
         + [Returning User](#returning-user)
         + [Site Owner](#site-owner)
   - [Design](#design)
      * [Colour Scheme](#colour-scheme)
      * [Typography](#typography)
      * [Imagery](#imagery)
      * [Interaction Feedback](#interaction-feedback)
      * [Icons](#icons)
   - [Wireframes](#wireframes)
      * [Deviations](#deviations)
   - [Database Models](#database-models)
   - [Features](#features)
      * [Technology Features](#technology-features)
      * [User Features](#user-features)
      * [Future Features](#future-featuresdevelopments)
      * [Design Features](#design-features)
   - [Technologies Used](#technologies-used)
      * [Languages Used](#languages-used)
      * [Frameworks, Libraries & Programs Used](#frameworks-libraries--programs-used)
   - [Testing](#testing)
   - [Deployment](#deployment)
      * [Creating a Gitpod Workspace](#creating-a-gitpod-workspace)
      * [GitHub Pages](#github-pages)
      * [Forking the GitHub Repository](#forking-the-github-repository)
      * [Making a Local Clone](#making-a-local-clone)
      * [Creating an application with Heroku](#creating-an-application-with-heroku)
   - [Credits](#credits)
      * [Code](#code)
      * [Content](#media)
      * [README](#readme)
         + [Inspiration](#inspiration)
         + [Mockup](#mockup)
      * [Acknowledgements](#acknowledgements)


# User Experience (UX)

- ## User stories

- ### First Time User

  1. As a First Time Visitor, I want to easily understand the main purpose of the web app.
  2. As a First Time Visitor, I want to be able to easily navigate the app and register my account.
  3. As a First Time Visitor, I want to be able to easily understand how to submit a question or reply to others questions

- ### Returning User

  1. As a Returning Visitor, I want to see if there are new questions being asked.
  2. As a Returning Visitor, I want to check my questions to see if they have been answered.

- ### Frequent User

  1. As a Frequent User, I want to be able to engage in discussions around specific topics.
  2. As a Frequent User, I want to be able to update my questions and answers or delete if necessary.

- ### Site Owner
   1. As site owner I want users to be able to submit, edit. and delete their own questions
   2. As site owner I want topic deletion to be limited to admins only
   3. As site owner I want the website to be responsive and display well on all devices for optimal UX. 


- # Design

- ## Colour Scheme

  - The main colours used are #fba018 (Primary Orange), #00008b (Primary blue and dark text colour), off-white #fafafa (250,250,250) (Used in a variety of ways adjusting transparency to adapt to different areas).
  - All colours tested on [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/) - all passed, though made adjustments such as not having blue on orange too much. Whilst it passes contrasting checks with flying colours, it isn't that pleasant to look at. 
  - Other colours were used for interaction feedback, such as Reds for delete buttons, darker oranges for hovers on buttons and lighter blues for the same purpose. 

- ## Typography

  - The Archivo Black (Google Font) is the main font used throughout fopr headings and emphasis text with Sans Serif as the fallback font in case for any reason the font isn't being imported into the site correctly. Archivo Black is easy to read, displays nicely and adds emphasis where necessary. 
  - Additional typography will all be sans-serif system fonts to allow for easy readability due to the nature of the site. 

- ## Imagery

  - **Masthead** - Image by Wirestock on [Freepik](https://www.freepik.com/free-photo/beautiful-shot-sydney-harbor-bridge-with-light-pink-blue-sky_10399362.htm)

  - Logo, mockups - all created by myself using Illustrator

- ## Interaction Feedback

  - Accent colours are used upon interaction such as hover and click to provide feedback to the user that they are interacting with an element, and that the element serves a purpose.
  - Flash messages used to notfiy users of errors or successes depending on outcome. Auto timeout included to avoid having to close every time. 

- ## Icons
   - Fontawesome Icons were used throughout the site including social links but also as interaction aids such as login and sign up buttons


# Wireframes

- All basic wireframes can be found here - [View](/downunder/static/readme/wireframe/ChatDownUnder.pdf)
   - ## Deviations
      - It should be noted that whilst the wireframes were implemented as part of the skeleton phase of UX planning at the outset, applying that 5 S's throughout led to some important amendments according to project scope and useability.

# Database Models 

- PDF example of my database models used can be found [here](/downunder/static/readme/database/CDU-DB-Diagram.pdf)


# Features

## Technology Features

- Responsive on all device sizes

- PSQL Relational Database

- Flask/SQLAlchemy used to implement CRUD functionality for users

- User ID's allow for user specific CRUD

- Modals used for defensive programming when it comes to item deletion

- Interaction feedback used throughout.

- Reply functionality enhances discussion experience

## User Features

**Key Features**

1. User registration, login and logout functionality
1. Submit questions for discussion
1. Tag questions with topics for easy navigation
1. Search bar that will find results if your search matches title, body or tags of a question
1. Add topics if you cannot find one relevant to your question
1. Reply to questions for a full discussion experience

## Future Features/Developments

1. Replying to replies - I would like to incorporate the logic for a user viewing their own question, to reply to answers given by the community. This will enhance user experience - at present they can add a comment but this may cause comment threads to get longer than they may need and out of control. Whereas if a user can reply directly to an answer it will keep it more strucutured. 

1. Add new Topic within Question (user feedback) - I tried several different routes but this was proving a little beyond scope for this project. I would like to incorporate the option so as when a user selects their topic, if a relevant topic is not present they can type their own, submit it and have it either dynamically update the list, so they can select their new topic, or submit the new topic as part of the form and have the backend handle the logic - I did trial this with a new topic as a separate option, but it caused the topic selector to become buggy and not perform as it should. Instead, I tried utilising AJAX to dynamically update the list, but again, this caused issue with Select2 and also continued to refresh the page making for a worse user experience. 

1. Search bar functionality - I would like to make the search more flexible, so if it finds "part" of the search term it will still return results as opposed to finding exact matches only

1. Image upload - allow users to upload images to their discussions - questions, replies etc. 

1. Profile picture - allow users to personalise their user profile further by adding a profile picture or avatar. 

1. Dedicated user profile area - perhaps incorporate a user profile page so users can see their questions, see if people have replied and also view their stats (how long they have been a member, how many questions they have asked, how many questions they have contributed to with answers etc.)

1. No Longer Urgent - have a button in view for the author of a question to click that will set is_urgent to false. This will allow for seamless changes if the question is answered or expired. 

1. Clickable topics - make topics on topic page and topic tags on questions clickable - taking users to a "results" page of relevant questions

1. Edit & Delete replies - give users the option to edit or delete their replies to questions

1. Reply counter and up-vote system - implement some sort of "like" or "upvote" system to rank replies and display highest ranking (most helpful) first. Also have a reply counter so users can see the size of a thread. 

## Design Features



# Technologies Used

## Languages Used

- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
- [Javascript](https://en.wikipedia.org/wiki/JavaScript)
- [Python](https://docs.python.org/3/)

## Frameworks, Libraries & Programs Used

1. [Bootstrap 4.4.1:](https://getbootstrap.com/docs/4.4/getting-started/introduction/)
   - Bootstrap was used to assist with the responsiveness and styling of the website.
2. [Jest:](https://jestjs.io/)
   - Jest was used to test the Javascript used
3. [SQLAlchemy:](https://docs.sqlalchemy.org/en/20/)
   - SQLAlchemy was used to communicate between the database and the frontend
4. [Google Fonts:](https://fonts.google.com/)
   - Google fonts were used to import the 'Archivo Black' font into the "Head" section of each html file which is used on all titles and emphasises throughout the project.
5. [Font Awesome:](https://fontawesome.com/)
   - Font Awesome was used throughout the website to add icons for aesthetic and UX purposes.
6. [jQuery:](https://jquery.com/)
   - jQuery came with Bootstrap to make the navbar responsive but was also used for Select2 
7. [Select2:](https://select2.org/)
   - Select2 was used for styling the dropdown and allowing for multiple selections without having to hold down CMD/CTRL or Shift
8. [FLASK:](https://flask.palletsprojects.com/)
   - Flask Frameworking was used to structure the site including the use of Jinja2 templating. Allowed for the smooth display of data from the backend. 
7. [Git](https://git-scm.com/)
   - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
8. [GitHub:](https://github.com/)
   - GitHub is used to store the projects code after being pushed from Git.
9. [Illustrator:](https://www.adobe.com/uk/products/illustrator.html)
   - Illustrator was used to create the logo
10. [Figma:](https://www.figma.com/)
      - Figma was used for all wireframing and flow illustration
11. [Youtube - TechWithTim:](https://www.youtube.com/@TechWithTim)
      - TechWithTim was a great help in understanding some of the more complex elements of Python programming and also in implementing my Login/Signup process
12. [StackOverflow:](https://stackoverflow.com/)
      - Used for code snippets and code validation, as well as tutorials and some vital help
13. [DBDiagram:](dbdiagram.io)
      - Used to generate database model diagrams

# Testing

A separate tests document has been added and can be found [here](TESTING.md). This includes details on user testing. There is also a test_app.py for testing the python when it came to adding, editing and deleting elements to avoid messing with the live preview. 


# Deployment

## Creating a Gitpod Workspace

The project was created in Gitpod using the Code Institute Gitpod Full Template using these steps:

1. Log in to GitHub and go to the [Code Institute student template for Gitpod](https://github.com/Code-Institute-Org/gitpod-full-template)
2. Click 'Use this Template' next to the Green Gitpod button.
3. Add a repository name and click 'Create reposiory from template'.
4. This will create a copy of the template in your own repository. Now you can click the green 'Gitpod' button to open a workspace in Gitpod.

## Forking the GitHub Repository

Forks are used to propose changes to someone else's project or to use someone else's project as a starting point for your own idea. By forking the GitHub Repository you make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository.

To Fork a Github Repository:

1. Log in to GitHub and go to the [GitHub Repository](https://github.com/Isabella-Mitchell/gather-recipe-website)
2. Locate the Fork button in the top-right corner of the page, click Fork.
3. You should now have a copy of the original repository in your GitHub account.

## Making a Local Clone

You will now have a fork of the repository, but you don't have the files in that repository locally on your computer.

To make a local clone:

1. Log in to GitHub and go to the [GitHub Repository](https://github.com/Isabella-Mitchell/gather-recipe-website)
2. Above the list of files, click  Code.
3. To clone the repository using HTTPS, under "Clone with HTTPS", click the 'Copy' icon. To clone the repository using an SSH key, including a certificate issued by your organization's SSH certificate authority, click Use SSH, then click the 'Copy' icon. To clone a repository using GitHub CLI, click Use GitHub CLI, then click the 'Copy' icon.
4. Open Git Bash.
5. Change the current working directory to the location where you want the cloned directory.
6. Type git clone, and then paste the URL you copied earlier. It will look like this, with your GitHub AE username instead of YOUR-USERNAME:

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
```

7. Press Enter. Your local clone will be created.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
> Cloning into `gather-recipe-website`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```

Click [Here](https://docs.github.com/en/github-ae@latest/get-started/quickstart/fork-a-repo) for the GitHub quick start guide with images and more detailed explanations of the above process.

## Creating an application with Heroku

You will need to deploy the application using Heroku.

1. Create a requirements.txt file by typing ``` pip3 freeze --local > requirements.txt ``` into the Gitpod CLI. Ensure this is added to your .gitignore file.
2. Create a Procfile by typing ```echo web: python app.py > Procfile```. Open it and ensure it doesn't have a new line, as this can create errors. Ensure it starts with a capital P.
3. Add and commit these files to Github.
4. Go to [Heroku](https://dashboard.heroku.com/apps). Log in or create an account
5. Click the 'New' button and click 'Create new app'.
6. Enter a unique name for your project with no capital letters or spaces and select your region. Click 'Create App'.
7. Inside your project, go to the Resources tab and create a Heroku Postgres Database
8. Inside your project, go to the 'Settings' tab. Scroll down and click 'Reveal Config Vars'.
9. Add in the following variables
  - IP : 0.0.0.0
  - PORT : 5000
  - MONGO_DBNAME : Your MongoDB database name
  - MONGO_URI : This can be found on MongoDB by going to Clusters, Connect, Connect to your application
  - SECRET_KEY : Your secret key
10. Deploy your project by going to the Deploy tab and choose 'Connect to Github'
11. Find your repository name and select Connect.
12. To connect your Heroku database, go to 'More' in the top right and select run console. Enter ```python3``` to access the python intepreter.
13. Then type ```From gather import db```. Then type ```db.create_all()```. You can then exit the console.


# Credits

## Code

- [Bootstrap4](https://getbootstrap.com/docs/4.4/getting-started/introduction/): Bootstrap Library used throughout the project mainly to make site responsive using the Bootstrap Grid System.

- [W3CSchools](https://www.w3schools.com/) W3C schools used for CSS/HTML confirmation

- [MDN Web Docs](https://developer.mozilla.org/) : For Pattern Validation code. Code was modified to better fit my needs and to match an Irish phone number layout to ensure correct validation. Tutorial Found [Here](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/tel#Pattern_validation)

- [StackOverflow](https://stackoverflow.com/) : For coding validation and tips on refining code. Also used for code snippets customised with my own css or JS.

- [CodePen](https://codepen.io/samueldthomas91/pen/oNJVxYx) : Codepen was used to explore examples of the game style I wanted to implement. I also used codepen to build my JS logic as it was easier to view and edit. My final codepen before transferring it back to codeanywhere can be found [HERE](https://codepen.io/samueldthomas91/pen/OJrKNgP)

- [TechWithTime](https://www.youtube.com/@TechWithTim) : Tech With Tim on youtube has a lot of valuable Python knowledge that I was able to adapt and utilise across my project

- [Miguel Grinberg](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-viii-followers) : This Flask Mega Tutorial was an incredible help with things such as understanding many to many relationships and fully utilising Flask app capabilities 

## Content

- Colour and content completely designed by myself

- Psychological properties of colours text in the README.md was found [here](http://www.colour-affects.co.uk/psychological-properties-of-colours)

- Colour combinations, hex code -> rgb conversion and palettes were found [here] (<https://www.colorhexa.com/>)

## Media

- Masthead backgroud image - [Freepik](https://www.freepik.com/free-photo/beautiful-shot-sydney-harbor-bridge-with-light-pink-blue-sky_10399362.htm#query=sydney&position=0&from_view=search&track=sph&uuid=ce4ecea8-9b88-4c4b-8630-f9f657464361)

## README

### Inspiration

- Inspiration was taken from Isabella Mitchell specifically her README for [Gather](https://github.com/Isabella-Mitchell/gather-recipe-website/blob/main/README.md?plain=1#user-experience)

### Mockup
- .ai file used for Mockup at the top of README file : Image by [Freepik](https://www.freepik.com/free-vector/flat-design-responsive-website-design_28747716.htm#query=multi%20device%20mockup&position=2&from_view=keyword&track=ais)

## Acknowledgements

- Tutor support at Code Institute for their support.

- Pasquale Fasulo for continuous helpful input and feedback

- Ben Smith for his support, input and feedback

- Miguel Grinberg for the vast knowledge on Flask

- Friends and family for valuable insights and feedback

- Isabella Mitchell for a well refined inspiration for my README and TESTING docs.