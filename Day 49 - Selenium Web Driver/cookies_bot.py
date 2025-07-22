import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


chrome_driver_path = "C:/Developement/chromedriver-win64/chromedriver.exe"

service = Service(executable_path=chrome_driver_path)
chrome_options = Options()

driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie_btn = driver.find_element(By.ID, "cookie")
store = driver.find_element(By.ID, "store")


timeout = time.time() + 60 * 5
five_sec_check = time.time() + 5

while time.time() < timeout:
    cookie_btn.click()
    if time.time() >= five_sec_check:
        five_sec_check = time.time() + 5
        available_items = store.find_elements(By.CSS_SELECTOR, "div:not(.grayed)")
        if available_items:
            available_items[-1].click()

try:
    cookie_per_second_element = driver.find_element(By.ID, "cps")
    cookie_per_second = cookie_per_second_element.text
    print(f"Final cookies/second: {cookie_per_second.split(': ')[1]}")
except Exception as e:
    print(f"Could not retrieve final cookies/second: {e}")
finally:

    driver.quit()
