from app.users.models import Users
from app.users.tests.test_setup import BaseTestCase


class TestModel(BaseTestCase):
    def test_user_model(self):
        user = Users(
            id=1, username="test_user", avatar_url="https://test-avatar-url.com",
            type="test_type", URL="https://test-url.com"
        )
        self.db.session.add(user)
        self.db.session.commit()

        queryset = Users.query.filter_by(id=1).first()

        self.assertEqual(queryset.id, 1)
        self.assertEqual(queryset.username, "test_user")
        self.assertEqual(queryset.avatar_url, "https://test-avatar-url.com")
        self.assertEqual(queryset.type, "test_type")
        self.assertEqual(queryset.URL, "https://test-url.com")
