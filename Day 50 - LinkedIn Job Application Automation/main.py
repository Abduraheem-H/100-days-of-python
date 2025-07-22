import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PHONE = "+251901229754"

chrome_driver_path = "C:/Developement/chromedriver-win64/chromedriver.exe"
service = Service(executable_path=chrome_driver_path)
options = Options()

driver = webdriver.Chrome(service=service, options=options)
driver.get(
    "https://www.linkedin.com/jobs/search/?currentJobId=4271184229&f_WT=2&geoId=100506914&keywords=python%20developer&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true"
)

wait = WebDriverWait(driver, 20)


modal_dismiss_button = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "button.modal__dismiss"))
)
modal_dismiss_button.click()
sign_in_button = driver.find_element(By.LINK_TEXT, "Sign in")
sign_in_button.click()

email = wait.until(EC.presence_of_element_located((By.ID, "username")))
email.send_keys("abdurahimhussein292@gmail.com")

password = driver.find_element(By.ID, "password")
password.send_keys("#samratat")

submit_btn = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
)
submit_btn.click()

time.sleep(5)


try:
    profile_icon = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "img.nav__avatar"))
    )
    if profile_icon:
        print("Login successful!")
except Exception as e:
    print("Login failed:", e)
    driver.quit()
    exit()


# apply for all jobs on the page
job_cards = driver.find_elements(By.CSS_SELECTOR, "li.jobs-search-results__list-item")
for job_card in job_cards:
    try:
        job_apply_button = job_card.find_element(
            By.CSS_SELECTOR, "button.jobs-apply-button"
        )
        job_apply_button.click()

        # Fill in the phone number
        phone_input = wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "input[name='phoneNumber']")
            )
        )
        phone_input.clear()
        phone_input.send_keys(PHONE)

        # Submit the application
        submit_application_button = wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "button[data-control-name='submit_unify']")
            )
        )
        submit_application_button.click()

        time.sleep(2)
    except Exception as e:
        print(f"Failed to apply for a job: {e}")

print("All applications submitted!")
