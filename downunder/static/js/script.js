// Add an auto close for flash messages
document.addEventListener('DOMContentLoaded', () => {
    setTimeout(() => {
        const flashMessage = document.querySelector('.flash-message');
        if (flashMessage) {
            flashMessage.style.transition = 'opacity 0.3s ease-out';
            flashMessage.style.opacity = '0';
            setTimeout(() => flashMessage.remove(), 200); // Use a fadeout for a smooth transition
        }
    }, 4000); // 4 seconds before fadeout
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

// Initialize select2

// $(document).ready(function () {
//     $('#question_topics').select2({
//         placeholder: "Select or add topics (up to 3)",
//         // enable tagging function ( https://stackoverflow.com/questions/53804359/allow-tags-in-select2-elements#:~:text=To%20enable%20tagging%2C%20set%20the%20tags%20option%20to%20true.&text=Note%20that%20when%20tagging%20is,the%20search%20box%20so%20far.)
//         tags: true,
//         tokenSeparators: [',', ' '],
//         // apply selection limit with Select2 (https://select2.org/selections)
//         maximumSelectionLength: 3,
//     });
// });

// Toggle the reply box display 
function showReplyForm(questionId) {
    let replyForms = document.querySelectorAll('.replyForm');
    replyForms.forEach(function(form) {
        if (form.getAttribute('data-question-id') === questionId) {
            form.classList.remove('d-none');
            form.classList.add('d-block');
        }
    });

}

function hideReplyForm(questionId) {
    let replyForms = document.querySelectorAll('.replyForm');
    replyForms.forEach(function(form) {
        if (form.getAttribute('data-question-id') === questionId) {
            form.classList.remove('d-block');
            form.classList.add('d-none');
        }
    });
}

module.exports = {
    showReplyForm,
    hideReplyForm
};