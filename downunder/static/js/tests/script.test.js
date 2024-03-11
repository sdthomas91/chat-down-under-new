/**
 * @jest-environment jsdom
 */


const { hideReplyForm, showReplyForm  } = require('../script.js');



describe('Reply Form Show/Hide Functionality', () => {
    // Setup DOM before each test
    beforeEach(() => {
      document.body.innerHTML = `
        <div class="replyForm d-none" data-question-id="1"></div>
        <div class="replyForm d-none" data-question-id="2"></div>
      `;
    });
  
    // Test showing the reply form
    test('showReplyForm should remove "d-none" and add "d-block" to the correct form', () => {
      showReplyForm('1');
  
      const form = document.querySelector('.replyForm[data-question-id="1"]');
      expect(form.classList.contains('d-none')).toBeFalsy();
      expect(form.classList.contains('d-block')).toBeTruthy();
    });
  
    // Test hiding the reply form
    test('hideReplyForm should remove "d-block" and add "d-none" to the correct form', () => {
      // display the form in order to test hiding
      showReplyForm('1');
  
      hideReplyForm('1');
  
      const form = document.querySelector('.replyForm[data-question-id="1"]');
      expect(form.classList.contains('d-block')).toBeFalsy();
      expect(form.classList.contains('d-none')).toBeTruthy();
    });
  
  });

 
  describe('Flash message fadeout and removal', () => {
    jest.useFakeTimers();
  
    beforeEach(() => {
      document.body.innerHTML = `<div class="flash-message">Message!</div>`;
    });
  
    test('Flash message fades out after 4 seconds and is removed after 200ms', () => {
      document.dispatchEvent(new Event('DOMContentLoaded'));
  
      // changed from execute all timers as this caused it to run the removal timer as well
      jest.advanceTimersByTime(4000);
  
      const flashMessage = document.querySelector('.flash-message');
  
      // Check if the flash message's style has been set to fade it out
      expect(flashMessage).not.toBeNull();
      expect(flashMessage.style.opacity).toBe('0');
      expect(flashMessage.style.transition).toBe('opacity 0.3s ease-out');
  
      // 200ms for removal
      jest.advanceTimersByTime(200);
  
      // Check if the flash message has been removed from the DOM
      expect(document.querySelector('.flash-message')).toBeNull();
    });
  
    // Clean up script
    afterEach(() => {
      jest.useRealTimers();
    });
  });
  
  describe('City Time Display Functionality', () => {
    beforeEach(() => {
        jest.useFakeTimers();
      // Mock the DOM structure
      document.body.innerHTML = `
        <div id="timePerth"></div>
        <div id="timeMelbourne"></div>
        <div id="timeSydney"></div>
        <div id="timeBrisbane"></div>
      `;
    });
  
    test('Displays the current times for major Australian cities', () => {
    
      document.dispatchEvent(new Event('DOMContentLoaded'));

      // Check each city's time display element for non-empty content
      const cities = ['Perth', 'Melbourne', 'Sydney', 'Brisbane'];
      cities.forEach(city => {
        const timeElement = document.getElementById(`time${city}`);
        expect(timeElement.textContent).not.toBe('');
  
      });
    });

  });
  