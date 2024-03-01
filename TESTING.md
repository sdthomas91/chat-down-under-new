<h1 align="center">Chat Down Under - Testing & Resolution</h1>

[View the live project here.]()

The purpose of this document is to identify key testing stages and instances where decisions were made to change or keep certain features.

## Bugs (All bugs now Resolved)

- Wanted to include a record of found and resolved bugs

1. One-to-many or many-to-many : Issues arose with my existing question model obtaining a topic_id. I had it set to a one-to-many relationship. Within user testing and error resolution I resolved that a many-to-many relationship makes more sense. This was users can select up to 3 topics relevant to their question, enhancing the filtering capabilities and reducing user difficulty in defining a single topic. 

1. 

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