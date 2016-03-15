import unittest
# local imports
import app


class AppTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.app.test_client()

    def test_root_url(self):
        rv = self.app.get('/')
        assert b'Homepage' in rv.data

if __name__ == '__main__':
    unittest.main()
