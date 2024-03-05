<h1 align="center">Chat Down Under - Testing & Resolution</h1>

[View the live project here.]()

The purpose of this document is to identify key testing stages and instances where decisions were made to change or keep certain features.

## Bugs (All bugs now Resolved)

- Wanted to include a record of found and resolved bugs

1. One-to-many or many-to-many : Issues arose with my existing question model obtaining a topic_id. I had it set to a one-to-many relationship. Within user testing and error resolution I resolved that a many-to-many relationship makes more sense. This was users can select up to 3 topics relevant to their question, enhancing the filtering capabilities and reducing user difficulty in defining a single topic. Found [this](https://support.microsoft.com/en-gb/office/video-create-many-to-many-relationships-e65bcc53-8e1c-444a-b4fb-1c0b8c1f5653#:~:text=A%20many%2Dto%2Dmany%20relationship%20exists%20when%20one%20or%20more,more%20items%20in%20another%20table.) very useful for learning how to create a many-to-many relationship. 

1. Topic Association - I decided to opt for a many-to-many relationship, which meant going with an association table in order to allow questions to be "Tagged" with different topics. However, whenever I try to pull the selected topics into a list it does not properly pull the information.
    - Tried disabling Select2 as assumed the Javascript may be intefering with the way the form was submitting this data as it was only the topics that were not translating - still bugging.
    - Realised I had left some historical code in from when I was attempting an "add new topic" functionality within the question form. Removed all "new_topic" code. Still bugging. 
    - Ran some debug code printing out selected topic id's, nothing. PRinted out the entire request.form and could see the information was there. However, the value of the topic id was being printed outside of the "selected_topic_id" list so it was never providing a value. 
    - Revised HTML and realised the name was set to "question_topics[]" which I know was correct for producing an array of items. However, I had forgotten to pass the same value in the route when adding the information. Amended from "selected_topic_ids = request.form.getlist('question_topics')" to "selected_topic_ids = request.form.getlist('question_topics[]')"
    - Topic ID's now being pulled an printed in front end where I had wanted them to. 

1. Edit question is_urgent - The logic implemented is not removing the is_urgent status of the question even if the box is unticked. 
    - I tried changing the form so it wasn't auto-selected from loading the edit_question section. However, the bug still persisted and it actually demeans the UX of the edit question flow. 
    - Tried changing backend logic so it could do a request to see if the is_urgent is on - then pass is_urgent as is_urgent so if it isn't "on" then it is false. This still failed. 
    - Realised I was overcomplicating things - removed the additional request and simply force set the is_urgent to false if it isn't present on the form (deselected). Now working as it should. 

# USER FEEDBACK 

##### User Feedback Implementations

1. After some user feedback it was decided that a more generalised searchability would better enhance the UX of the site

    - Used advanced routing and the ilike() python method to implement a more robust and flexible search experience for users allowing for the system to compare their search term to title, body and topics instead of just topics.   

1. One piece of user feedback suggested implementing some sort of world clock so people could see the time in different parts of australia compared to UK time

    - Utilised Javascript to display world clocks according to different parts of Australia (major cities)

1. Some users fedback that they didn't fully understand the purpose or layout of the site upon first visit.

    - Added an about us page to avoid confusion and aid user experience. Also added prompts and clear titles so each section was fairly transparent on it's purpose and display


# SECTION TESTING

## Header

### Navigation

- Standard navigation featured left aligned menu; amended this to ensure centre alignment for easy viewing.
- Decided against the use of an "about" element in the navigation as it is fairly self explanatory - however, I plan to implement an about page and include it in a footer link section
- Modified code - originally had signup, login and logout all displaying. For user experience I decided to implement some Jinja templating to ensure that if you are logged in you only see logout and vice versa. Other nav elements are for logged in users only such as submitting a question so used python to implement that logic in routes. 

#### Layout

- Grid system was glitchy and caused elements to overlap on smaller screens and increase display past viewport width. Refactored the grid for smaller screens and now flows nicely. 

### Masthead (base.html)

1. Search bar
    - originally intended to have a search bar in which you could search for topics. However, after some user feedback it was decided that a more generalised searchability would better enhance the UX of the site. That is to say, rather than taking a topic as a search term, I will endeavour to use the search to return results that contain the search in their title, body or topics to allow for greater search functionality. 
    - 

1. Image

   - Main image : was not displaying well behind text and cause contrasting issues. Applied an overlay to ensure text was still fully readable. 

1. Timezones : 

   - One piece of user feedback suggested implementing some sort of world clock so people could see the time in different parts of australia compared to UK time - implemented using vanilla JS and included JEST testing within the script.test.js file.

   - Faced some issues with JEST testing due to timeout errors - instead tested via user feedback and console check. All timezones now display correctly and increment on the minute rather than the second as this was a bit of a visual overload. 

1. Image height - implemented different viewport stylings to allow for a larger image on mobile view to encompass the world clocks. Otherwise it overlapped and spilt over into main content. 


## Topics

### Add topics


## Questions

### Add new question

- Originally designed the form using bootstrap but for authentication and ease of use I decided to implement a Flask form. It didn't respond as nicely across viewports so added some bootstrap via spans to allow for a nicer user experience. 

- Finally resolved the issues with the many-to-many relationship. Main issue encountered was trying to maintain a standard one-to-many relationship without realising. I left the topic_id in as an individual requirement whilst also trying to use the association table to connect the multiple topics to the question. 

- I decided to display the question in such a way that it shows title, body, tags and author. This allows for good community interaction. 

### View on homepage

For this element I wanted to allow logged in users to view their profile information alongside the most recent questions - similar to the styling of Reddit and other discussion forums. 

- Using bootstrap I implemented a column system that allowed for questions to stack within the latest question section and also to the right in a smaller section include user profile information. 

### Footer

#### Layout

- Decided to go for a table layout in the footer for a modern display. Played with several options including multi column for helpful links but there aren't enough navigation items to justify as this stage. 

# ELEMENT TESTING

## Buttons (outside of standard buttons)

## UX

### Error Checking

#### HTML Validation

- Included below are screenshots of errors found - all rectified accordingly. This involded changing "id" on modals/forms to avoid duplicates, adding alt attributes (or correcting from alt-text to alt) and other general fixes.
  | HTML Validation Errors | - | - |
  | -------------------- | :---------------: | :---------------: |
  | ![Html Errors 1](/assets/images/error-html-1.png) | ![Html Errors 2](/assets/images/error-html-2.png) |![Html Errors 3](/assets/images/error-html-3.png) |
  | ![Html Errors 4](/assets/images/error-html-4.png) | ![Html Errors 5](/assets/images/error-html-5.png) ||

- Errors were all addressed and corrected accordingly - html trial code has been moved to this document for reference only
  | HTML Validation Errors Corrected |
  | -------------------- |
  | ![Html Errors Corrected](/assets/images/no-error-html.png) |

  - Validation carried out for contact-success.html and was all clear

#### CSS Validation

- All CSS clear - validation passed
  | Validated CSS |
  | -------------------- |
  | ![CSS No Errors](/assets/images/no-error-css.png) |

## Unused Code

#### New Question and Edit question 

- I opted to not use the code to process a neew topic being added during the question submission. Having [researched](https://wpmudev.com/blog/load-posts-ajax/#:~:text=AJAX%20(Asynchronous%20JavaScript%20and%20XML,all%20without%20reloading%20the%20page.) and thinking about a modal I discoverd an AJAX process that would allow me to open a modal with the add_topic template, add the topic and then dynamically update the form so users don't have to navigate away from the form in order to update. Unused code in routes.py : 
    ```python
        #Additional logic for new topic handling
        if 'new_topic' in selected_topic_ids:
            #added strip to make new topic compatible
            new_topic_name = request.form.get('new_topic_name').strip()
            if new_topic_name:
                new_topic = Topic(topic_name=new_topic_name)
                db.session.add(new_topic)
                """(https://www.geeksforgeeks.org/
                file-flush-method-in-python/) Several resources used to find 
                the correct option - decided on flush(). I needed a function 
                that would register the value of a new topic without
                completing the form submission in order to allow all 
                selected topics to be added first. I believe this was the
                most effective way of achieving this """
                db.session.flush() 
                new_question.topics.append(new_topic)

- Also decided against the dynamic modal I had planned on using: 
   
```html
    <!-- ADD TOPIC MODAL  -->
  <div class="modal fade" id="addTopicModal" tabindex="-1" role="dialog" aria-labelledby="modalLabel"
    aria-hidden="true">
    <div class="modal-dialog" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="modalLabel">Add New Topic</h5>
          <button type="button" class="close" data-dismiss="modal" aria-label="Close">
            <span aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body">
          <!-- Form for adding new topic -->
          <form id="addTopicForm">
            <div class="form-group">
              <label for="topicName">Topic Name</label>
              <input type="text" class="form-control" id="topicName" name="topicName" required>
            </div>
            <button type="submit" class="btn btn-primary">Add Topic</button>
          </form>
        </div>
      </div>
    </div>
  </div>
  <!-- Add topic modal -->