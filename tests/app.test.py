import unittest
from flask import session
#
from code.app import app
from code.user import User

class UserTest(unittest.TestCase):
    # get the app test client
    def setUp(self):
        self.test_client = app.test_client()

    # clear the testing databse
    def tearDown(self):
        db = _get_db()
        db.client.drop_database(db)

    def user_dict(self):
        return dict(
            username="jorge",
            password="test123"
            )

    def test_register_user(self):
        # basic registration
        rv = self.app.post('/register', data=self.user_dict(), follow_redirects=True)
        assert User.objects.filter(username=self.user_dict()['username']).count() == 1

        # Invalid username characters
        user2 = self.user_dict()
        user2['username'] = "test test"
        user2['email'] = "test@example.com"
        rv = self.app.post('/register', data=user2, follow_redirects=True)
        assert "Invalid username" in str(rv.data)

        # Is username being saved in lowercase?
        user3 = self.user_dict()
        user3['username'] = "TestUser"
        user3['email'] = "test2@example.com"
        rv = self.app.post('/register', data=user3, follow_redirects=True)
        assert User.objects.filter(username=user3['username'].lower()).count() == 1

        # confirm the user
        user = User.objects.get(username=self.user_dict()['username'])
        code = user.change_configuration.get('confirmation_code')
        rv = self.app.get('/confirm/' + user.username + '/' + code)
        assert "Your email has been confirmed" in str(rv.data)

        # try again to confirm
        rv = self.app.get('/confirm/' + user.username + '/' + code)
        assert rv.status_code == 404

        # check change configuration is empty
        user = User.objects.get(username=self.user_dict()['username'])
        assert user.change_configuration == {}

    def test_login_user(self):
        # create user
        self.app.post('/register', data=self.user_dict())
        # login user
        rv = self.app.post('/login', data=dict(
            username=self.user_dict()['username'],
            password=self.user_dict()['password']
            ))
        # check the session is set
        with self.app as c:
            rv = c.get('/')
            assert session.get('username') == self.user_dict()['username']