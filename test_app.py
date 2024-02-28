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

if __name__ == '__main__':
    unittest.main()