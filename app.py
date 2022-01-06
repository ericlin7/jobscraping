from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

# direct webdriver where the browser file is:
driver_path = "geckodriver.exe"
driver = webdriver.Firefox(executable_path=driver_path)

# your secret credentials:
email = "wangmaria923@gmail.com"
password = "74$ppkt!"

# login linkedin
driver.get('https://www.linkedin.com/login')
time.sleep(3)
driver.find_element_by_id('username').send_keys(email)
driver.find_element_by_id('password').send_keys(password)
driver.find_element_by_id('password').send_keys(Keys.RETURN)


driver.get("https://www.linkedin.com/jobs/")
time.sleep(3)
# find the keywords/location search bars:
search_bars = driver.find_elements_by_class_name('jobs-search-box__text-input')
search_keywords = search_bars[0]
search_keywords.send_keys(keywords)
    
search_location = search_bars[2]
search_location.send_keys(location)
search_location.send_keys(Keys.RETURN)

