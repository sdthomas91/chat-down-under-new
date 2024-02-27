<h1 align="center">Chat Down Under - A Discussion Forum for all things Australia Migration</h1>

[View the live project here.](!!!INSERT HEROKU LINK HERE""")

This is a dicussion forum using a relational database that will allow users to proactively discuss topics regarding migrating to Australia. 

Utilising Bootstrap row/column tool the site will present responsively and in a well structured, readable, easy to navigate way so as to allow maximum UX. Using python the site will be structured in such a way that users will be able to log in, submit their question and review answers that others may have given on those questions. User authentication will allow users to view, edit and delete their questions, as well as view, edit and delete their responses to others questions. 

The app will be rigorously User Tested and will be deployed to Heroku for online access. 

<h2 align="center"><img src="assets/images/braintrainer-mockup.jpg"></h2>

## Future Developments

1. Comment replies - I would like to incorporate the logic for a user viewing their own question, to reply to answers given by the community. This will enhance user experience - at present they can add a comment but this may cause comment threads to get longer than they may need and out of control. Whereas if a user can reply directly to an answer it will keep it more strucutured. 


## Known Bugs

1.

## User Experience (UX)

- ### User stories

- #### First Time Visitor Goals

  1. As a First Time Visitor, I want to easily understand the main purpose of the web app.
  2. As a First Time Visitor, I want to be able to easily navigate the app and register my account.
  3. As a First Time Visitor, I want to be able to easily understand how to submit a question or reply to others questions

- #### Returning Visitor Goals

  1. As a Returning Visitor, I want to see if there are new questions being asked.
  2. As a Returning Visitor, I want to check my questions to see if they have been answered.

- #### Frequent User Goals

  1. As a Frequent User, I want to be able to engage in discussions around specific topics.
  2. As a Frequent User, I want to be able to update my questions and answers or delete if necessary.

- ### Design

- #### Colour Scheme

  - The main colours used are #f47d15 (Interaction Feedback), #4b0066 (Main Colour), #f1a906 (Secondary colour - headings etc.) and off-white #f9f9f9 (Light).
  - All colours tested on WebAIM Contrast Checker - some changes were made, including making #4b0066 the main colour due to it's good contrast with all other colours.

    <img src="assets/images/colour-palette.png">

- #### Typography

  - The Kavoon font is the main font used throughout the whole website with Sans Serif as the fallback font in case for any reason the font isn't being imported into the site correctly. Kavoon provides a fun, game style font whilst maintaining a good level of readability for accessibility purposes.
  - Additional typography where needed (game instructions etc.) will be a simple Sans Serif font such as Verdana.

- #### Imagery

  - All images created by myself including logo, card logo, card contents.

- #### Interaction Feedback

  - Accent colours are used upon interaction such as hover and click to provide feedback to the user that they are interacting with an element, and that the element serves a purpose.
  - Sound effects are used to enhance the game experience on flipping, correct match, incorrect match and game completion.
  - Animation used for the card flip to give it a realistic feel rather than just flicking from one image to the next. Makes the game feel better quality and more enjoyable/pleasant to play.

## Wireframes

- All basic wireframes can be found here - [View](https://www.figma.com/file/zAQX9o6OAKkXcJyxj9RKId/BrainTrainer-Wireframe?type=design&node-id=0-1&mode=design)

### Deviations

It should be noted that whilst the wireframes were implemented as part of the skeleton phase of UX planning at the outset, applying that 5 S's throughout led to some important amendments to increase functionality. I also realised that having originally planned for multiple levels, this was going to impact timeframes and mean the quality of the work may suffer. Further levels could be added as a later version, but for the scope and timeframe of this project I decided to stick with one level, with the interaction feedback explaining as much (prompts when clicking on locked levels etc.)

## Features

- Responsive on all device sizes

- Advanced Javascript providing a smooth interactive gaming experience

- Ability to progress and improve by competing against your own time

- ID's used in order to access DOM and manipulate date

- Modals used to instructions to avoid unncessary navigation away from the main page

- Tiles used to illustrate a clear journey through levels etc.

- Interaction feedback used throughout - this includes all clickable buttons/links, cards, sound effects, animations.

- Leaderboard allows players to rank themselves (functionality to be improved in later versions)

### User Feedback Implementations

- A number of users fedback that they would rather the music play across all pages and maintain the functionality to toggle music on and off. Gentle piano music used as it can aid memory function and concentration.
- Issues with logo sizing impacting game view on smaller devices - used image and text combination with bootstrap responsive options to display each respectively. This allows for a more seamless cross platform experience.
- Clearer notice that level is locked upon click and also when game was completed - originally had an alert but decided to use a modal and implement some logic to show the modal automatically once each relevant trigger was found.
- Some users noted that occasionally after resetGame the checkForMatch wouldn't work properly and reset button would be required to ensure smooth gameplay. Combatted largley by rearranging functions and removing some unnecessary code that I was unaware of.
- Some users fedback that they were unsure which direction the progression would be on the homepage. Whilst it is not completely relevant for the current release I would address these concerns by adding some css to incorporate some sort of dashed line from level to level to show progression direction.
- Some users have fedback that on some mobile devices they cannot see the bottom elements of the gameboard such as the best time and attmepts whilst playing the game. however, gameboard and timerare visible so not a major issue. Could reduce pdding or margins in future versions to improve this.

## Technologies Used

### Languages Used

- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
- [Javascript](https://en.wikipedia.org/wiki/JavaScript)

### Frameworks, Libraries & Programs Used

1. [Bootstrap 4.4.1:](https://getbootstrap.com/docs/4.4/getting-started/introduction/)
   - Bootstrap was used to assist with the responsiveness and styling of the website.
2. [Jest](https://jestjs.io/)
   - Jest was used to continuously test and grow my code and functions
3. [Hover.css:](https://ianlunn.github.io/Hover/)
   - Hover.css was used on the Social Media icons in the footer to add the float transition while being hovered over.
4. [Google Fonts:](https://fonts.google.com/)
   - Google fonts were used to import the 'Kavoon' font into the "Head" section of each html file which is used on all pages throughout the project.
5. [Font Awesome:](https://fontawesome.com/)
   - Font Awesome was used throughout the website to add icons for aesthetic and UX purposes.
6. [jQuery:](https://jquery.com/)
   - jQuery came with Bootstrap to make the navbar responsive but was also used for the smooth scroll function in JavaScript.
7. [Git](https://git-scm.com/)
   - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
8. [GitHub:](https://github.com/)
   - GitHub is used to store the projects code after being pushed from Git.
9. [Illustrator:](https://www.adobe.com/uk/products/illustrator.html)

- Illustrator was used to create the logo and card fronts.

10. [Figma:](https://www.figma.com/)

- Figma was used to create the wireframes during the design process.

11. [CSSGradient](https://cssgradient.io/)

- CSSGradient.io was used to generate css gradient backgrounds.

12. [StackOverflow](https://stackoverflow.com/)

- Used for code snippets and code validation, as well as tutorials and some vital help

## Testing

A separate tests document has been added to showcase the Javascript testing - this can be found in the scripts directory. I also duplicated the script document which can be found is game.js - this was to avoid having to remove event listeners and comment out exports etc. for published site to run effectively but also to make testing easier.

I was unable to complete JEST tests for all functions due to time constraints. I got very caught up in the JEST side of things as it was very new to me. A lot of stackOverflow help and youtube videos were needed to understand some of the more complex elements of the tests. There are still some elements that I don't fully grasp but all functions tested now pass. I did manage to test all CORE functions relating to gameplay. The only functions left out were the updating the best time and also toggling the music. Both were suitably tested through user testing though.

Remaining functions were still tested through user testing and the game proves to function well.

- Little to no HTML CSS testing was required due to the simplicity of the web pages - still validated through W3C validator as listed below.

The W3C Markup Validator and W3C CSS Validator Services were used to validate every page of the project to ensure there were no syntax errors in the project.

- [W3C Markup Validator](https://validator.w3.org/nu/#textarea) :

| index.html                                      | level-1.html                                        | leaderboard.html                                            |
| ----------------------------------------------- | --------------------------------------------------- | ----------------------------------------------------------- |
| ![index.html](assets/images/index-html-val.png) | ![level-1.html](assets/images/level-1-html-val.png) | ![leaderboard.html](assets/images/leaderboard-html-val.png) |

- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) - - all clear
- ![style.css](assets/images/CSS-val.png)

### Testing User Stories from User Experience (UX) Section

- #### First Time Visitor Goals

  1. As a First Time Visitor, I want to easily understand the main purpose of the game and understand how to play.

     1. Upon entering the site, users are automatically greeted with a clean and easily readable navigation bar which clearly showcases a How To Play button and a help button.
     2. The How to Play button opens a readable modal with clear text in the same window to minimise navigation away from the page
     3. The instructions are thorought and clear
     4. The help button gives the opportunity to request further help if still unsure

  2. As a First Time Visitor, I want to be able to easily navigate the game and start a game with ease.

     1. The game board is laid out nicely on the home page allowing easy access to all areas of the site
     2. Leaderboard navigation accessible and consistent header/nav on all pages allow UI friendly navigation process
     3. Game accessible via tiles and easy navigation to either homepage or leaderboard from there.

  3. As a First Time Visitor, I want to be able to easily understand what will happen when I interact with areas of the site

     1. The user has immediate navigational ability to reach the leaderboard, toggle music and access help/how to
     2. Constant user feedback either by sound effect or css effecvs allows the user to understand what can be interacted with and how it will behave

- #### Returning Visitor Goals

  1. As a Returning Visitor, I want to see if there are new levels available.

     1. The homepage showcases all levels and clearly notifies when a level is locked or available
     2. The obvious help option allows users to contact to request new levels or ask if anything new is available

  2. As a Returning Visitor, I want to check my previous scores.

     1. The level page will contain the existing high score and allow it to be over written if the new score is better
     2. The leaderboard houses some stock scores but also logs the users high score for them to see how they are progressing

- #### Frequent User Goals

  1. As a Frequent User, I want to be able to continuously improve upon my previous score.

     1. The opportunity to log your high score, view it and improve upon it allows users to compete against themselves to continuously improve their speed and memory

  2. As a Frequent User, I want to be able to progress.

     1. The option to climb the leaderboard rankings provides a way of the user measuring success and progression
     2. Future developments will see extra level which will allow the user to move through harder challenges and progress both in the game and personally

### Further Testing

- The Website was tested on Google Chrome, Microsoft Edge and Safari browsers. It was also tested in Internet Explorer Mode on Microsoft Edge. There were some issues regarding autoplay on the audio but nothing that would effect gameplay
- The website was viewed on a variety of devices such as HP Windows Desktop, Macbook, iMac, iPhone12, iPhone 14 Pro, iPhone 8, iPad Air, iPad Pro 12.9", Pixel 5, Samsung Galaxy S20 Ultra, Surface Pro 7 and Nest Hub. Responsiveness was patchy to begin with but using Bootstrap it now presents nicely across all platforms.
- A large amount of testing was done to ensure that all user interactions both on home page and during gameplay were smooth and consistent.
- Friends and family members were asked to review the site and documentation to point out any bugs and/or user experience issues.

#### Google Lighthouse

- Google Lighthouse was used to ensure compatability, best practice and accessibility as well as load times.

| index.html                                        | level-1.html                                          | leaderboard.html                                              |
| ------------------------------------------------- | ----------------------------------------------------- | ------------------------------------------------------------- |
| ![index.html](assets/images/index-lighthouse.png) | ![level-1.html](assets/images/level-1-lighthouse.png) | ![leaderboard.html](assets/images/leaderboard-lighthouse.png) |

##### Load Speed

- Results were fairly good for all pages with 73% + all round. Slowest was level 1 for the obvious reason that it has the highest JS content.

##### Accessibility

- Accessibility sits at 100 for all pages bar the leaderboard - not a big issue but complaints of headings not being sequencial but it is not relevant for this page.

##### Best Practices

- Best Practices sits at 92 out of 100 - there was one error, JS error logged to console. I cannot seem to get rid of these errors.

## Deployment

### GitHub Pages

The project was deployed to GitHub Pages using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/sdthomas91/ng-spmu-milestone)
2. At the top of the Repository (not top of page), locate the "Settings" Button on the menu.
   - Alternatively Click [Here](https://raw.githubusercontent.com/) for a GIF demonstrating the process starting from Step 2.
3. Scroll down the Settings page until you locate the "GitHub Pages" Section.
4. Under "Source", click the dropdown called "None" and select "Master Branch".
5. The page will automatically refresh.
6. Scroll back down through the page to locate the now published site [link](https://github.com/sdthomas91/ng-spmu-milestone) in the "GitHub Pages" section.

### Forking the GitHub Repository

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/sdthomas91/ng-spmu-milestone)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/sdthomas91/ng-spmu-milestone)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

```
git clone https://github.com/sdthomas91/ng-spmu-milestone
```

7. Press Enter. Your local clone will be created.

```
$ git clone https://github.com/sdthomas91/ng-spmu-milestone
> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```

Click [Here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) to retrieve pictures for some of the buttons and more detailed explanations of the above process.

## Credits

### Code

- [Bootstrap4](https://getbootstrap.com/docs/4.4/getting-started/introduction/): Bootstrap Library used throughout the project mainly to make site responsive using the Bootstrap Grid System.

- [W3CSchools](https://www.w3schools.com/) W3C schools used for CSS/HTML confirmation

- [MDN Web Docs](https://developer.mozilla.org/) : For Pattern Validation code. Code was modified to better fit my needs and to match an Irish phone number layout to ensure correct validation. Tutorial Found [Here](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/tel#Pattern_validation)

- [StackOverflow](https://stackoverflow.com/) : For coding validation and tips on refining code. Also used for code snippets customised with my own css or JS.

- [CodePen](https://codepen.io/samueldthomas91/pen/oNJVxYx) : Codepen was used to explore examples of the game style I wanted to implement. I also used codepen to build my JS logic as it was easier to view and edit. My final codepen before transferring it back to codeanywhere can be found [HERE](https://codepen.io/samueldthomas91/pen/OJrKNgP)

### Content

- Colour and content completely designed by myself

- Psychological properties of colours text in the README.md was found [here](http://www.colour-affects.co.uk/psychological-properties-of-colours)

- Colour combinations, hex code -> rgb conversion and palettes were found [here] (<https://www.colorhexa.com/>)

### Media

- Masthead backgroud image - [Freepik](https://www.freepik.com/free-photo/beautiful-shot-sydney-harbor-bridge-with-light-pink-blue-sky_10399362.htm#query=sydney&position=0&from_view=search&track=sph&uuid=ce4ecea8-9b88-4c4b-8630-f9f657464361)

### Audio

- Error Sound : Sound effect from [PixaBay](https://pixabay.com/sound-effects/?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=7184)
- Correct Sound : Sound effect from [PixaBay](https://pixabay.com/?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=6033)
- Winning Sound : [UppBeat](https://uppbeat.io/browse/sfx/celebrate)
- Background Music : license included in assets/copyright

#### README Mockup

- .ai file used for Mockup at the top of README file : Image by [Freepik](https://www.freepik.com/free-vector/flat-design-responsive-website-design_28747716.htm#query=multi%20device%20mockup&position=2&from_view=keyword&track=ais)

### Acknowledgements

- Tutor support at Code Institute for their support.

- Pasquale Fasulo for continuous helpful input and feedback

- My mentor, Gurjot for continued input and direction

- © 2014 Nate Wiley CodePen for the initial inspiration

- Friends and family for valuable insights and feedback