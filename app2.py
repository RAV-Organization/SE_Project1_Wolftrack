from flask import Flask, render_template, request, jsonify
import subprocess
import json

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('recommended_jobs.html')


@app.route('/recommended_jobs_results', methods=['POST'])
def search():
    job_title = request.form['job_title']
    location = request.form['location']

    # Run your scraping script with the given job title and location
    subprocess.run(['python', 'jobscraping.py', job_title, location])

    # Load the data from the JSON file
    with open('jobs_data.json', 'r') as json_file:
        jobs_data = json.load(json_file)

    return jsonify(jobs_data)


if __name__ == '__main__':
    app.run(debug=True)
