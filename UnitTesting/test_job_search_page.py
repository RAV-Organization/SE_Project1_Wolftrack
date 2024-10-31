# tests/test_job_search_page.py

import json
import pytest


def test_job_search_page(client):
    """Test the job search page renders correctly."""
    response = client.get('/student/job_search')
    assert response.status_code == 200
    assert b'Job Search' in response.data  # Check if the page title is present
    assert b'Job Title' in response.data  # Ensure input fields are rendered
    assert b'Location' in response.data  # Ensure input fields are rendered


def test_job_search_form_submission(client, mocker):
    """Test the job search form submission."""
    mock_response = [
        {
            "job_title": "Software Engineer",
            "company_name": "Tech Company",
            "location": "Raleigh, NC",
            "job_link": "https://www.indeed.com/job/software-engineer"
        },
        {
            "job_title": "Data Scientist",
            "company_name": "Data Inc.",
            "location": "Raleigh, NC",
            "job_link": "https://www.indeed.com/job/data-scientist"
        }
    ]

    # Mock the endpoint that processes the form submission
    mocker.patch('your_project.app.scraping_search',
                 return_value=json.dumps(mock_response))

    # Perform the form submission
    response = client.post('/student/job_search/result', data={
        'job_title': 'Software Engineer',
        'location': 'Raleigh'
    })

    assert response.status_code == 200
    jobs_data = json.loads(response.data)
    assert isinstance(jobs_data, list)  # Ensure the response is a list
    assert len(jobs_data) == 2  # Check the number of jobs returned
    # Check first job title
    assert jobs_data[0]['job_title'] == 'Software Engineer'
    # Check second job title
    assert jobs_data[1]['job_title'] == 'Data Scientist'
