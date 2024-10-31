import unittest
from app import app  # Replace with your Flask app file name


class TestResourcesTabRoute(unittest.TestCase):
    def setUp(self):
        app.testing = True  # Enable testing mode
        self.client = app.test_client()  # Create a test client

    def test_resources_tab_route(self):
        # Send a GET request to the route
        response = self.client.get('/student/resources_tab')

        # Check that the request was successful (status code 200)
        self.assertEqual(response.status_code, 200)

        # Check for the presence of key elements
        self.assertIn(b'Job Resources', response.data)  # Page title
        self.assertIn(b'Select Job Role:', response.data)  # Dropdown label
        self.assertIn(b'Software Engineer', response.data)  # Dropdown option
        self.assertIn(b'Machine Learning Engineer',
                      response.data)  # Dropdown option
        self.assertIn(b'Data Analyst', response.data)  # Dropdown option

        # Check specific sections for different job roles
        self.assertIn(b'Resources for Software Engineers', response.data)
        self.assertIn(
            b'Resources for Machine Learning Engineers', response.data)
        self.assertIn(b'Resources for Data Analysts', response.data)

    def test_software_engineer_resources(self):
        # Check specific resources within the Software Engineer section
        response = self.client.get('/student/resources_tab')
        self.assertIn(b'Learn JavaScript', response.data)
        self.assertIn(b'System Design Basics', response.data)

    def test_ml_engineer_resources(self):
        # Check specific resources within the Machine Learning Engineer section
        response = self.client.get('/student/resources_tab')
        self.assertIn(
            b'Deep Learning Specialization by Andrew Ng', response.data)
        self.assertIn(b'Machine Learning with Python', response.data)

    def test_data_analyst_resources(self):
        # Check specific resources within the Data Analyst section
        response = self.client.get('/student/resources_tab')
        self.assertIn(b'Data Visualization with Python', response.data)
        self.assertIn(b'SQL for Data Analysis', response.data)


if __name__ == '__main__':
    unittest.main()
