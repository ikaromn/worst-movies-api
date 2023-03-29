from unittest import TestCase

from app import create_app


class TestApiRoutes(TestCase):
    def setUp(self):
        self.app = create_app().test_client()

    def test_home(self):
        """
        Tests the home route
        """
        rv = self.app.get("/")
        result = rv.get_json()
        print(result)
        self.assertDictEqual({"Hello": "World"}, result)
