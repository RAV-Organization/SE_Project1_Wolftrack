import pytest
import json

def test_resources_tab(client):
    """Test the resources tab route."""
    response = client.get('/student/resources_tab')
    assert response.status_code == 200
    assert b'Resources' in response.data  # Check for specific content


def test_job_search(client):
    """Test the job search route."""
    response = client.get('/student/job_search')
    assert response.status_code == 200
    assert b'Job Search' in response.data  # Check for specific content


def test_scraping_search(client, mocker):
    """Test the scraping search functionality."""
    mocker.patch('subprocess.run')  # Mock subprocess call
    response = client.post('/student/job_search/result', data={
        'job_title': 'Software Engineering',
        'location': 'Raleigh'
    })
    assert response.status_code == 200
    jobs_data = json.loads(response.data)
    assert isinstance(jobs_data, list)  # Ensure it's a list
    assert 'job_title' in jobs_data[0]  # Check for expected key
