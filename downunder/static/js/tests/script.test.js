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

    jest.useFakeTimers();

test('should remove the flash message after 3 seconds', () => {
    require('../script.js'); 
    const flashMessage = document.querySelector('.flash-message');

    expect(flashMessage).not.toBeNull();

    // Fast-forward until all timers have been executed
    jest.runAllTimers();

    // Now that the timers have been fast-forwarded, check the condition
    expect(document.querySelector('.flash-message')).toBeNull();
});
});
