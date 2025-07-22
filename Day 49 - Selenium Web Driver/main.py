from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

chrome_driver_path = "C:/Developement/chromedriver-win64/chromedriver.exe"

service = Service(executable_path=chrome_driver_path)
chrome_options = Options()

driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get("https://www.python.org/")

selected_elements = driver.find_elements(
    by="css selector", value=".event-widget .menu li"
)

my_dict = {}
for count, element in enumerate(selected_elements):
    time_elements = element.find_elements(by="tag name", value="time")
    a_element = element.find_elements(by="tag name", value="a")
    try:
        my_dict[count] = {
            "time": time_elements[0].text,
            "name": a_element[0].text,
        }
    except (IndexError, ValueError):
        continue
driver.quit()

print(my_dict)
