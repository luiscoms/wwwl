import unittest
# local imports
from src import app

__export__ = ['AppTestCase']


class AppTestCase(unittest.TestCase):

    def test_root_url(self):
        with app.test_client() as client:
            rv = client.get('/')
        assert b'Homepage' in rv.data

if __name__ == '__main__':
    unittest.main()
