import unittest
import base64
# local imports
from app import app
import json


class LunchTestCase(unittest.TestCase):

    def request(self, client, uri, username, password):
        user_pass_bytes = bytes("{0}:{1}".format(username, password), 'ascii')
        headers = {
            'Authorization': 'Basic ' +
            base64.b64encode(user_pass_bytes).decode('ascii')
        }
        return client.open(uri, headers=headers)

    def test_get_all_lunches(self):
        """Test the list of lunches."""

        with app.test_client() as client:
            # rv = client.get('/lunches', None)
            user_pass_bytes = bytes('username:password', 'ascii')
            rv = self.request(client, '/lunches', 'username', 'password')

        self.assertEqual(200, rv.status_code)

        retstr = str(rv.data.decode('ascii'))

        expect = json.dumps({
            "lunches": [{

                "date": "2016-03-16 00:00:00",
                "place": "Nice place"
            }]
        })

        self.assertEqual(expect, retstr)

    def test_get_lunches_by_date(self):
        """Test filtered lunches."""

        with app.test_client() as client:
            rv = client.get('/lunches/2016-03-01')

        # expect no content
        self.assertEqual(204, rv.status_code)

        with app.test_client() as client:
            rv = client.get('/lunches/2016-13-01')

        # expect not found
        self.assertEqual(404, rv.status_code)

        with app.test_client() as client:
            rv = client.get('/lunches/2016-03-16')

        self.assertEqual(200, rv.status_code)

        retstr = str(rv.data.decode('ascii'))

        expect = json.dumps({
            "lunch": {

                "date": "2016-03-16 00:00:00",
                "place": "Nice place"
            }
        })

        self.assertEqual(expect, retstr)

if __name__ == '__main__':
    unittest.main()
