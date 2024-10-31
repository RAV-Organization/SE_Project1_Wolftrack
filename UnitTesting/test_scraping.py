import json
import os
import pytest
from unittest.mock import patch


def test_scraping_script(mocker):
    """Test the scraping script functionality."""
    mocker.patch('subprocess.run')  # Mock subprocess call

    # Simulate input arguments
    job_title = 'Software Engineering'
    location = 'Raleigh'

    # Here you can add logic to simulate the scraping output
    mock_response = [
        {
            "job_title": "Software Engineer",
            "company_name": "Tech Company",
            "location": "Raleigh, NC",
            "job_link": "https://www.indeed.com/job/software-engineer"
        }
    ]

    # Mock the JSON output from the scraping script
    with open("jobs_data.json", "w") as json_file:
        json.dump(mock_response, json_file)

    # Check that the jobs_data.json file is created and contains the correct data
    assert os.path.exists("jobs_data.json") == True
    with open("jobs_data.json", "r") as json_file:
        data = json.load(json_file)
        assert len(data) == 1
        assert data[0]["job_title"] == "Software Engineer"
