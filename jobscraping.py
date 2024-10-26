from bs4 import BeautifulSoup
from lxml import etree as et
from csv import writer
import time
from time import sleep
import pandas as pd
from random import randint
import json

import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import sys

service = ChromeService(
    r"C:\\Users\\bihan\\Downloads\\chromedriver-win64\\chromedriver.exe")

option = webdriver.ChromeOptions()
option.add_argument("--incognito")
# option.add_argument("--headless")
# option.add_argument("--start-minimized")
# option.add_argument("--headless=new")
option.add_argument("--window-position=2000,0")

service.start()
driver = webdriver.Remote(service.service_url, options=option)


# job_ = 'Content Writing'
# location = 'New+York'

job_ = sys.argv[1] if len(sys.argv) > 1 else 'Engineering'
location = sys.argv[2] if len(sys.argv) > 2 else 'Raleigh'


# driver.get(paginaton_url.format(job_, location, 0))

paginaton_url = 'https://www.indeed.com/jobs?q={}&l={}&radius=35'
driver.get(paginaton_url.format(job_, location))
# driver.get('http://www.google.com/')

soup = BeautifulSoup(driver.page_source, 'html.parser')

jobs_data = []

# Loop through each <li> element with the specified classes
for li in soup.find_all('li', class_='css-1ac2h1w eu4oa1w0'):
    job_title_elem = li.find(
        'span', {'id': lambda x: x and x.startswith('jobTitle')})
    job_title = job_title_elem.get_text(strip=True) if job_title_elem else None

    company_name = li.find('span', {'data-testid': 'company-name'}).get_text(
        strip=True) if li.find('span', {'data-testid': 'company-name'}) else None

    location = li.find('div', {'data-testid': 'text-location'}).get_text(
        strip=True) if li.find('div', {'data-testid': 'text-location'}) else None

    job_link = 'https://www.indeed.com' + job_title_elem.find_parent(
        'a')['href'] if job_title_elem and job_title_elem.find_parent('a') else None

    # if job_title:
    #     print(f"Job Title: {job_title}")
    # if company_name:
    #     print(f"Company Name: {company_name}")
    # if location:
    #     print(f"Location: {location}")
    # if job_link:
    #     print(f"Job Link: {job_link}")

    # print("\n")
    
    if job_title:
        jobs_data.append({
            "job_title": job_title,
            "company_name": company_name,
            "location": location,
            "job_link": job_link
        })

# Save jobs data to JSON file
with open("jobs_data.json", "w") as json_file:
    json.dump(jobs_data, json_file, indent=4)

print("Job data saved to jobs_data.json")


time.sleep(15)
driver.quit()
