import json
import os
import pytest
from unittest.mock import patch


def test_scraping_script(mocker):
    mocker.patch('subprocess.run')  

    job_title = 'Software Engineering'
    location = 'Raleigh'

    mock_response = [
        {
            "job_title": "Software Engineer",
            "company_name": "Tech Company",
            "location": "Raleigh, NC",
            "job_link": "https://www.indeed.com/job/software-engineer"
        }
    ]

    with open("jobs_data.json", "w") as json_file:
        json.dump(mock_response, json_file)

    assert os.path.exists("jobs_data.json") == True
    with open("jobs_data.json", "r") as json_file:
        data = json.load(json_file)
        assert len(data) == 1
        assert data[0]["job_title"] == "Software Engineer"
