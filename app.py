from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

# direct webdriver where the browser file is:
s = Service('/Users/jiayuetian/Downloads/chromedriver')
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