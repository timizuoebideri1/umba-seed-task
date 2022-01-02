from app.users.models import Users
from app.users.tests.test_setup import BaseTestCase, create_user


class TestModel(BaseTestCase):
    def test_user_model(self):
        create_user(self)

        queryset = Users.query.filter_by(id=1).first()

        self.assertEqual(queryset.id, 1)
        self.assertEqual(queryset.username, "test_user")
        self.assertEqual(queryset.avatar_url, "https://test-avatar-url.com")
        self.assertEqual(queryset.type, "test_type")
        self.assertEqual(queryset.URL, "https://test-url.com")
