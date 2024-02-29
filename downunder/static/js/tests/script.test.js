/**
 * @jest-environment jsdom
 */

describe('Flash Message Fade Out', () => {
    beforeEach(() => {
        // Setup the DOM environment
        document.body.innerHTML = `
            <div class="flash-message">This is a flash message!</div>
        `;
    });

    test('should fade out and remove the flash message after 3 seconds', (done) => {
        require('../script.js'); 

        const flashMessage = document.querySelector('.flash-message');

        // Check if the flash message exists and has not faded out immediately
        expect(flashMessage).not.toBeNull();
        expect(flashMessage.style.opacity).toBe('');

        // Wait for the fade-out effect to start
        setTimeout(() => {
            expect(flashMessage.style.opacity).toBe('0');
            expect(flashMessage.style.transition).toContain('opacity 0.3s ease-out');

            // Wait for the flash message to be removed
            setTimeout(() => {
                expect(document.querySelector('.flash-message')).toBeNull();
                done();
            }, 300); 
        }, 3000); 
    });
});
