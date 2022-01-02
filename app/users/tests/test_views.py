from app.users.tests.test_setup import BaseTestCase, create_user


class TestView(BaseTestCase):
    def test_users_route(self):
        create_user(self)  # create user
        req = self.client.get("/")

        self.assertEqual(req.status_code, 200)
        self.assertEqual('test_user' in str(req.data), True)
