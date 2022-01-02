from flask import url_for

from app.users.tests.test_setup import BaseTestCase, create_user


class TestApi(BaseTestCase):
    def setUp(self):
        super().setUp()
        users_id = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        for user_id in users_id:
            create_user(self, user_id)

    def test_users_api(self):
        req = self.client.get(url_for('usersapi'))

        self.assertEqual(req.status_code, 200)
        self.assertEqual(len(req.json.get("result")), 10)

    def test_users_api_with_pagination(self):
        url = url_for('usersapi', pagination=5)
        req = self.client.get(url)

        self.assertEqual(req.status_code, 200)
        self.assertEqual(len(req.json.get("result")), 5)
        self.assertEqual(req.json.get("total"), 10)
        self.assertEqual(req.json.get("prev_url"), '')
        self.assertIn(url_for('usersapi', page=2, pagination=5), req.json.get("next_url"))

    def test_users_api_page_not_found(self):
        url = url_for('usersapi', pagination=10, page=2)
        req = self.client.get(url)

        self.assertEqual(req.status_code, 404)
        self.assertIn("The requested URL was not found", req.json.get("message"))

