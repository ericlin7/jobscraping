from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import csv

s = Service('./chromedriver')
driver = webdriver.Chrome(service=s)

# your secret credentials:
email = "wangmaria923@gmail.com"
password = "74$ppkt123"

keywords = "Software"
location = "Toronto"

# Go to linkedin and login
driver.get('https://www.linkedin.com/login')
time.sleep(3)
driver.find_element(By.ID, 'username').send_keys(email)
driver.find_element(By.ID,'password').send_keys(password)
driver.find_element(By.ID,'password').send_keys(Keys.RETURN)

driver.get("https://www.linkedin.com/jobs/")
time.sleep(3)

# find the keywords/location search bars:
search_keywords = driver.find_element(By.ID,'jobs-search-box-keyword-id-ember30')
search_keywords.send_keys(keywords) 
search_location = driver.find_element(By.ID,'jobs-search-box-location-id-ember30')
search_location.send_keys(location + Keys.ENTER)

# make beautifulsoup object
job_src = driver.page_source  
soup = BeautifulSoup(job_src, 'lxml')  

# job_title
jobs_html = soup.find_all('a', {'class': 'job-card-list__title'})
job_titles = []
for title in jobs_html:
    job_titles.append(title.text.strip())  

# company_name
company_name_html = soup.find_all(
  'div', {'class': 'job-card-container__company-name'})
company_names = []
for name in company_name_html:
    company_names.append(name.text.strip()) 

# job description
time.sleep(3)
job_details = []
list_items = driver.find_elements_by_class_name("occludable-update")
for job in list_items:
    job.click()
    time.sleep(3)
    details = driver.find_element(By.ID,"job-details").text
    job_details.append(details)

job_list = zip(job_titles, company_names, job_details)

# put into CSV file -> MySQL
with open('test.csv', 'w', newline="") as f:
    writer = csv.writer(f)
    writer.writerow(job_list)