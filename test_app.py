import unittest # using pythons unittest documentation (https://docs.python.org/3/library/unittest.html)
from downunder import app, db
from downunder.models import User
#add forgotten password_hash necessities 
from werkzeug.security import generate_password_hash, check_password_hash

class UserTestCase(unittest.TestCase):
    def setUp(self):
        """
        Test application configuration
        """
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db' #using sqlite for ease of use
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False  #disable CSRF tokens for testing
        self.client = app.test_client()

        # Test database creation 
        with app.app_context():
            db.create_all()

    def tearDown(self):
        """
        Use tearDown to clean up database after each test
        """
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_sign_up(self):
        """
        POST request data sample 
        """
        data = {
            'email': 'test@example.com',
            'username': 'testuser',
            'fname': 'Test',
            'lname': 'User',
            'password1': 'securepassword',
            'password2': 'securepassword'
        }

        response = self.client.post('/sign_up', data=data, follow_redirects=True)
        
        # Successful sign up with flash message check 
        self.assertIn(b'Account Created! Please proceed to login', response.data)

        # Verify that the user was added to the database
        with app.app_context():
            user = User.query.filter_by(email='test@example.com').first()
            self.assertIsNotNone(user)
            self.assertTrue(check_password_hash(user.password, 'securepassword'))

    def test_submit_question(self):
        """
        Test the question submission process
        """
        # First, create a user and log them in
        user_data = {
            'email': 'user@example.com',
            'username': 'user',
            'fname': 'User',
            'lname': 'Example',
            'password1': 'password',
            'password2': 'password'
        }
        self.client.post('/sign_up', data=user_data, follow_redirects=True)
        self.login('user@example.com', 'password')

        # Create a topic for the question to be associated with
        with app.app_context():
            new_topic = Topic(topic_name="Test Topic")
            db.session.add(new_topic)
            db.session.commit()
            topic = Topic.query.filter_by(topic_name="Test Topic").first()

        # Now submit a question
        response = self.submit_question(
            question_title="Test Question",
            question_body="This is a test question.",
            topic_ids=[str(topic.id)]
        )

        # Check for successful submission message
        self.assertIn(b'Your question has been added!', response.data)

        # Verify that the question was added to the database
        with app.app_context():
            question = Question.query.filter_by(question_title="Test Question").first()
            self.assertIsNotNone(question)
            self.assertEqual(question.question_body, "This is a test question.")
            self.assertEqual(question.topics[0].topic_name, "Test Topic")
            self.assertEqual(question.author.username, 'user')


        
if __name__ == '__main__':
    unittest.main()