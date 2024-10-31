import unittest
from app import app  # Replace with your actual app file name

class StatsPageTestCase(unittest.TestCase):
    def setUp(self):
        # Set up the test client
        self.app = app.test_client()
        self.app.testing = True

    def test_stats_page_status_code(self):
        # Test if the /stats route is accessible
        response = self.app.get('/stats')
        self.assertEqual(response.status_code, 200)

    def test_stats_page_content(self):
        # Test if the /stats page has specific content indicating the chart
        response = self.app.get('/stats')
        self.assertIn(b'Current Salary Posting', response.data)
        self.assertIn(b'Salaries for Software Development Role', response.data)
        self.assertIn(b'Companies', response.data)

if __name__ == "__main__":
    unittest.main()
