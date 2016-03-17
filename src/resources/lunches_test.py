import unittest
import base64
# local imports
from src import app
import json


class LunchTestCase(unittest.TestCase):

    def request(self, method, uri, username, password, data=None):
        """Return an opened request using username and passoword."""
        user_pass_bytes = bytes("{0}:{1}".format(username, password), 'ascii')
        headers = {
            'Authorization': 'Basic ' +
            base64.b64encode(user_pass_bytes).decode('ascii')
        }

        with app.test_client() as client:
            return client.open(uri, method=method, headers=headers, data=data)

    def test_get_all_lunches(self):
        """Test the list of lunches."""
        rv = self.request('get', '/lunches', 'hungryemployee', 'iamhungry')

        self.assertEqual(200, rv.status_code)

        retstr = str(rv.data.decode('ascii'))

        expect = json.dumps({
            "lunches": [{
                "date": "2016-03-16 00:00:00",
                "votes": [{
                    "username": "hungryemployeetwo",
                    "place": "Nice place"
                }]
            }]
        })

        self.assertEqual(expect, retstr)

    def test_get_lunches_by_date(self):
        """Test filtered lunches."""
        rv = self.request('get', '/lunches/2016-03-01', 'hungryemployee', 'iamhungry')

        # expect no content
        self.assertEqual(204, rv.status_code)

        rv = self.request('get', '/lunches/2016-13-01', 'hungryemployee', 'iamhungry')

        # expect not found
        self.assertEqual(404, rv.status_code)

        rv = self.request('get', '/lunches/2016-03-16', 'hungryemployee', 'iamhungry')
        self.assertEqual(200, rv.status_code)

        retstr = str(rv.data.decode('ascii'))

        expect = json.dumps({
            "lunch": {
                "date": "2016-03-16 00:00:00",
                "votes": [{
                    "username": "hungryemployeetwo",
                    "place": "Nice place"
                }]
            }
        })

        self.assertEqual(expect, retstr)

    def test_votes(self):
        """Test votes on places."""
        expect = json.dumps({
            "lunch": {
                "date": "2016-03-17 00:00:00",
                "votes": [{
                    "username": "hungryemployeetwo",
                    "place": "Really Nice place"
                }]
            }
        })

        data = json.dumps({
            "username": "hungryemployeetwo",
            "place": "Really Nice place"
        })

        rv = self.request('post', '/lunches/2016-03-17/votes', 'hungryemployeetwo', 'iamhungry', data)

        self.assertEqual(201, rv.status_code)
        retstr = str(rv.data.decode('ascii'))
        self.assertEqual(expect, retstr)

        rv = self.request('post', '/lunches/2016-03-17/votes', 'hungryemployeetwo', 'iamhungry', data)
        self.assertEqual(400, rv.status_code)

        data = json.dumps({
            "username": "hungryemployee",
            "place": "Really Nice place"
        })

        rv = self.request('post', '/lunches/2016-03-17/votes', 'hungryemployeetwo', 'iamhungry', data)
        self.assertEqual(201, rv.status_code)

        expect = json.dumps({
            "lunch": {
                "date": "2016-03-17 00:00:00",
                "votes": [{
                    "username": "hungryemployeetwo",
                    "place": "Really Nice place"
                },
                {
                    "username": "hungryemployee",
                    "place": "Really Nice place"
                }]
            }
        })

        retstr = str(rv.data.decode('ascii'))
        self.assertEqual(expect, retstr)


if __name__ == '__main__':
    unittest.main()
