import json
import os


def test_json_output_format():
    """Test the format of the JSON output."""
    with open("jobs_data.json", "r") as json_file:
        data = json.load(json_file)
        assert isinstance(data, list) 
        for job in data:
            assert "job_title" in job
            assert "company_name" in job
            assert "location" in job
            assert "job_link" in job
