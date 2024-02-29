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
document.addEventListener('DOMContentLoaded', function() {
    const updateTime = () => {
        // Simple minute and hour display - no need for seconds, was too busy
        const options = { hour: '2-digit', minute: '2-digit' };

        // Timezones required for the display
        const timeZones = {
            Perth: 'Australia/Perth',
            Melbourne: 'Australia/Melbourne',
            Sydney: 'Australia/Sydney',
            Brisbane: 'Australia/Brisbane'
        };

        // Set time for each city listed 
        for (const [city, timeZone] of Object.entries(timeZones)) {
            const timeString = new Intl.DateTimeFormat('en-AU', { ...options, timeZone }).format(new Date());
            document.getElementById(`time${city}`).textContent = timeString;
        }
    };

    // Update time every minute
    updateTime();
    setInterval(updateTime, 60000);
});