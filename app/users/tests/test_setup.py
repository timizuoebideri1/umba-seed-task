import unittest

from app.main import create_app, db
from app.main.config import configuration


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.db = db
        self.app = create_app(configuration['testing'])
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()
        self.db.create_all()

    def tearDown(self):
        self.db.session.remove()
        self.db.drop_all()
        self.app_context.pop()
