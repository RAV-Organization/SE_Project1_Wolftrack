from app import app, db
from flask_testing import TestCase
from unittest.mock import patch
import unittest
import json


class TestFlaskApp(TestCase):

    def create_app(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///:memory:"
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_resources_tab(self):
        """Test the resources tab route."""
        response = self.client.get('/student/resources_tab')
        self.assert200(response)
        self.assertIn(b'Resources', response.data)

    def test_job_search(self):
        """Test the job search route."""
        response = self.client.get('/student/job_search')
        self.assert200(response)
        self.assertIn(b'Job Search', response.data)

    @patch('subprocess.run')
    def test_scraping_search(self, mock_subprocess):
        """Test the scraping search functionality with mock subprocess."""
        mock_subprocess.return_value = None  
        response = self.client.post('/student/job_search/result', data={
            'job_title': 'Software Engineering',
            'location': 'Raleigh'
        }, follow_redirects=True)
        self.assert200(response)
        jobs_data = json.loads(response.data)
        self.assertIsInstance(jobs_data, list)
        if jobs_data:
            self.assertIn('job_title', jobs_data[0])  


if __name__ == '__main__':
    unittest.main()
