import $ from 'jquery';
import 'select2';

// Initialize select2

$(document).ready(function () {
    $('#question_topics').select2({
        placeholder: "Select or add topics (up to 3)",
        // enable tagging function ( https://stackoverflow.com/questions/53804359/allow-tags-in-select2-elements#:~:text=To%20enable%20tagging%2C%20set%20the%20tags%20option%20to%20true.&text=Note%20that%20when%20tagging%20is,the%20search%20box%20so%20far.)
        tags: true,
        tokenSeparators: [',', ' '],
        // apply selection limit with Select2 (https://select2.org/selections)
        maximumSelectionLength: 3,
    });
});

// AJAX call to dynamically update the topics list 
$('#addTopicForm').submit(function(event) {
    event.preventDefault(); // Prevent the default form submission

    var formData = $(this).serialize(); // Serialize the form data

    $.ajax({
        type: 'POST',
        url: '/add_topic', // Adjust if your route differs
        data: formData,
        success: function(response) {
            // Assuming the server responds with the new topic's ID and name
            if(response.topicId && response.topicName) {
                // Append the new topic to the Select2 dropdown
                var newOption = new Option(response.topicName, response.topicId, true, true);
                $('#question_topics').append(newOption).trigger('change');

                // Optionally, clear the input field in the modal
                $('#topicName').val('');
            }
        },
        error: function(xhr, status, error) {
            // Handle errors (e.g., topic already exists)
            console.error("Error adding topic:", error);
        }
    });
});

// Add an auto close for flash messages
document.addEventListener('DOMContentLoaded', () => {
    setTimeout(() => {
        const flashMessage = document.querySelector('.flash-message');
        if (flashMessage) {
            flashMessage.style.transition = 'opacity 0.3s ease-out';
            flashMessage.style.opacity = '0';
            setTimeout(() => flashMessage.remove(), 200); // Use a fadeout for a smooth transition
        }
    }, 2000); // 2 seconds before fadeout
});

// Add a time function that displays the times for major cities in Australia 
document.addEventListener('DOMContentLoaded', function () {
    const updateTime = () => {
        // Simple minute and hour display - no need for seconds, was too busy
        const options = {
            hour: '2-digit',
            minute: '2-digit'
        };

        // Timezones required for the display
        const timeZones = {
            Perth: 'Australia/Perth',
            Melbourne: 'Australia/Melbourne',
            Sydney: 'Australia/Sydney',
            Brisbane: 'Australia/Brisbane'
        };

        // Set time for each city listed 
        for (const [city, timeZone] of Object.entries(timeZones)) {
            const timeString = new Intl.DateTimeFormat('en-AU', {
                ...options,
                timeZone
            }).format(new Date());
            document.getElementById(`time${city}`).textContent = timeString;
        }
    };

    // Update time every minute
    updateTime();
    setInterval(updateTime, 60000);
});


// Allow customers to open a "new Topic" input to add a new topic to the topics database
document.addEventListener('DOMContentLoaded', () => {
    const topicSelect = document.getElementById('question_topics');
    const newTopicGroup = document.getElementById('new_topic_name_group');

    topicSelect.addEventListener('change', () => {
        const selected = Array.from(topicSelect.options).some(option => option.value === "new_topic" && option.selected);
        newTopicGroup.style.display = selected ? 'block' : 'none';
    });
});