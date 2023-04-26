import unittest
from app import app


class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_get_rate_date(self):
        response = self.app.get('/exchanges/aud/2023-04-24')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Code: aud', response.get_data(as_text=True))
        self.assertIn('Date: 2023-04-24', response.get_data(as_text=True))
        self.assertIn('Average:', response.get_data(as_text=True))

    def test_get_rate_date_error(self):
        response = self.app.get('/exchanges/xxx/2023-01-01')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_data(as_text=True), 'Data not found')

    def test_get_rate_date_invalid_input(self):
        response = self.app.get('/exchanges/aud/2024-08-45')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_data(as_text=True), 'Data not found')

    def test_get_rate_minmax(self):
        response = self.app.get('/minmax/eur/20')
        self.assertEqual(response.status_code, 200)
        self.assertIn('min rate:', response.get_data(as_text=True))
        self.assertIn('max rate:', response.get_data(as_text=True))

    def test_get_rate_minmax_invalid_N(self):
        response = self.app.get('/minmax/eur/0')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_data(as_text=True), 'Error: N value must be between 1 and 255 only.')

    def test_get_rate_max_difference(self):
        response = self.app.get('/difference/eur/10')
        self.assertEqual(response.status_code, 200)
        self.assertIn('max difference:', response.get_data(as_text=True))


if __name__ == '__main__':
    unittest.main()
