import unittest
from app import app


class TestResourcesTabRoute(unittest.TestCase):
    def setUp(self):
        app.testing = True  
        self.client = app.test_client()  

    def test_resources_tab_route(self):
        response = self.client.get('/student/resources_tab')

        self.assertEqual(response.status_code, 200)

        self.assertIn(b'Job Resources', response.data)  
        self.assertIn(b'Select Job Role:', response.data)
        self.assertIn(b'Software Engineer', response.data)
        self.assertIn(b'Machine Learning Engineer',
                      response.data)  
        self.assertIn(b'Data Analyst', response.data)

        self.assertIn(b'Resources for Software Engineers', response.data)
        self.assertIn(
            b'Resources for Machine Learning Engineers', response.data)
        self.assertIn(b'Resources for Data Analysts', response.data)

    def test_software_engineer_resources(self):
        response = self.client.get('/student/resources_tab')
        self.assertIn(b'Learn JavaScript', response.data)
        self.assertIn(b'System Design Basics', response.data)

    def test_ml_engineer_resources(self):
        response = self.client.get('/student/resources_tab')
        self.assertIn(
            b'Deep Learning Specialization by Andrew Ng', response.data)
        self.assertIn(b'Machine Learning with Python', response.data)

    def test_data_analyst_resources(self):
        response = self.client.get('/student/resources_tab')
        self.assertIn(b'Data Visualization with Python', response.data)
        self.assertIn(b'SQL for Data Analysis', response.data)


if __name__ == '__main__':
    unittest.main()
