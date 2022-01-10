from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import csv
import mysql.connector
import pandas as pandasForSortingCSV

email = input("Please enter email: ")

password = input("Please enter password: ")

keywords = input("Please enter job title you are looking for: ")

location = input("Please type in your location: ")

skills = []
user = input("Enter Skills type x to stop: ")

while(user != "x"):
    user = input("Enter Skills type x to stop: ")
    skills.append(user)

skills.pop()

print("Let's find your jobs! :)")

s = Service('./chromedriver')
driver = webdriver.Chrome(service=s)

'''
# your secret credentials:
email = "wangmaria923@gmail.com"
password = "74$ppkt123"

keywords = "Software intern"
location = "Vancouver"
skills = ["Scala", "Java", "React/Redux", "HTML", "CSS", "JavaScript", "C++", "Python", "SQL"]
'''

# Go to linkedin and login
driver.get('https://www.linkedin.com/login')
time.sleep(3)
driver.find_element(By.ID, 'username').send_keys(email)
driver.find_element(By.ID,'password').send_keys(password)
driver.find_element(By.ID,'password').send_keys(Keys.RETURN)

driver.get("https://www.linkedin.com/jobs/")
time.sleep(3)

# find the keywords/location search bars:
search_keywords = driver.find_element(By.CLASS_NAME,'jobs-search-box__text-input')
search_keywords.send_keys(keywords + Keys.TAB + location + Keys.ENTER) 
#search_location = driver.find_element(By.CLASS_NAME,'jobs-search-box__text-input')
#search_location.send_keys(location + Keys.ENTER) 

# job description
time.sleep(3)
job_titles = []
company_names = []
job_details = []
skill_match = []
list_items = driver.find_elements_by_class_name("occludable-update")
count = 0
for job in list_items:
    job.click()
    time.sleep(3)
    details = driver.find_element(By.ID,"job-details").text 
    for a in skills:
        if (a in details):
            skill_match.append(a)        
    job_details.append(skill_match.copy())
    skill_match.clear()
    count += 1
    if (count == 25):
        job_src = driver.page_source  
        soup = BeautifulSoup(job_src, 'lxml')  
        time.sleep(5)

        # job_title
        jobs_html = soup.find_all('a', {'class': 'job-card-list__title'})
        for title in jobs_html:
            job_titles.append(title.text.strip())  

        # company_name
        company_name_html = soup.find_all('a', {'class': 'job-card-container__company-name'})
        for name in company_name_html:
            company_names.append(name.text.strip()) 
print(company_names)
job_list = zip(job_titles, company_names, job_details)
zipped = list(job_list)
print(zipped)
# put into CSV file -> MySQL
with open('{}.csv'.format(email), 'w', newline="") as f:
    writer = csv.writer(f)
    list = [location]
    writer.writecol(list)
    for job in zipped:
        for a in job:
            writer.writerow(a)


csvData = pandasForSortingCSV.read_csv('{}.csv'.format(email))
print(csvData)

csvData.sort_values()

