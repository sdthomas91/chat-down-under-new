// Add an auto close for flash messages
document.addEventListener('DOMContentLoaded', () => {
    setTimeout(() => {
        const flashMessage = document.querySelector('.flash-message');
        if (flashMessage) {
            flashMessage.style.transition = 'opacity 0.3s ease-out';
            flashMessage.style.opacity = '0';
            setTimeout(() => flashMessage.remove(), 300); // Use a fadeout for a smooth transition
        }
    }, 3000); // 3 seconds before fadeout
});