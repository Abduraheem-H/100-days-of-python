import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

chrome_driver_path = "C:/Developement/chromedriver-win64/chromedriver.exe"
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode


service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get("https://forms.gle/Kjv4PWfEXaPEoq4MA")
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Cache-Control": "max-age=0",
}

response = requests.get(
    url="https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D",
    headers=headers,
)
# print(f"Response status code: {response.status_code}")

soup = BeautifulSoup(response.text, "html.parser")

property_cards = soup.select("ul.photo-cards > li:not(.nav-ad-empty)")
print(f"Total listings found: {len(property_cards)}")

properties = []
for item in property_cards:
    address_element = item.find("address")
    price_element = item.select_one('[data-test="property-card-price"]')
    link_element = item.find("a", {"href": True})
    if not address_element or not price_element or not link_element:
        continue
    try:
        address = address_element.getText(strip=True)
        price = (
            price_element.getText(strip=True).split("+")[0].split("/")[0]
            if price_element
            else "N/A"
        )
        property_link = link_element.get("href")
        if not property_link.startswith("http"):
            property_link = "https://www.zillow.com" + property_link
        properties.append(
            {
                "address": address,
                "price": price,
                "link": property_link,
            }
        )
    except Exception as e:
        print(f"Error extracting data: {e}")
        continue

print(f"Total properties extracted: {len(properties)}")

for prop in properties:
    input_fields = driver.find_elements(By.CSS_SELECTOR, ".Xb9hP input[type='text']")
    if len(input_fields) >= 3:
        input_fields[0].send_keys(prop["address"])
        input_fields[1].send_keys(prop["price"])
        input_fields[2].send_keys(prop["link"])
    driver.find_element(By.CSS_SELECTOR, "span.NPEfkd").click()
    driver.implicitly_wait(15)  # Wait for the form to submit
    driver.find_element(By.LINK_TEXT, "ሌላ ምላሽ አስገባ").click()
    driver.implicitly_wait(5)  # Wait for the form to reset

print("Data submitted successfully.")
driver.quit()
