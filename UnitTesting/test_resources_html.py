import unittest
from app import app  # Assuming your app is named app.py


class ResourcesTabTestCase(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    def test_resources_tab_route(self):
        # Test the /student/resources_tab route status code
        response = self.client.get('/student/resources_tab')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Job Resources', response.data)

    def test_dropdown_present(self):
        # Test that the job role dropdown is present in the response
        response = self.client.get('/student/resources_tab')
        self.assertIn(b'Select Job Role:', response.data)
        self.assertIn(
            b'<option value="software-engineer">Software Engineer</option>', response.data)
        self.assertIn(
            b'<option value="ml-engineer">Machine Learning Engineer</option>', response.data)
        self.assertIn(
            b'<option value="data-analyst">Data Analyst</option>', response.data)

    def test_software_engineer_section(self):
        # Test for specific content in the Software Engineer resources section
        response = self.client.get('/student/resources_tab')
        self.assertIn(b'Resources for Software Engineers', response.data)
        self.assertIn(b'Learn JavaScript', response.data)
        self.assertIn(b'System Design Basics', response.data)

    def test_ml_engineer_section(self):
        # Test for specific content in the Machine Learning Engineer resources section
        response = self.client.get('/student/resources_tab')
        self.assertIn(
            b'Resources for Machine Learning Engineers', response.data)
        self.assertIn(
            b'Deep Learning Specialization by Andrew Ng', response.data)
        self.assertIn(b'Machine Learning with Python', response.data)

    def test_data_analyst_section(self):
        # Test for specific content in the Data Analyst resources section
        response = self.client.get('/student/resources_tab')
        self.assertIn(b'Resources for Data Analysts', response.data)
        self.assertIn(b'Data Visualization with Python', response.data)
        self.assertIn(b'SQL for Data Analysis', response.data)


if __name__ == '__main__':
    unittest.main()
