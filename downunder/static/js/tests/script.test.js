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
 