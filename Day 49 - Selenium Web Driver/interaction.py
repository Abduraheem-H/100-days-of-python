from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:/Developement/chromedriver-win64/chromedriver.exe"

service = Service(executable_path=chrome_driver_path)
chrome_options = Options()

driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name_input = driver.find_element(By.NAME, "fName")
first_name_input.send_keys("Abdurahim")


last_name_input = driver.find_element(By.NAME, "lName")
last_name_input.send_keys("Muzemil")


email_name = driver.find_element(By.NAME, "email")
email_name.send_keys("sample@gmail.com")

button = driver.find_element(By.TAG_NAME, "button")
button.click()


import time

time.sleep(3)
