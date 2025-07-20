import smtplib
from bs4 import BeautifulSoup
import requests
import os


URL = "https://www.amazon.com/Apple-iPhone-13-128GB-Blue/dp/B09LNCFWVV/ref=sr_1_1?crid=2B2N3WXBB1GS5&dib=eyJ2IjoiMSJ9.Rw9FniwTzwW4jPB70gMLvGpX8kDe5A5soESClI76Jt2fPh_d_bIwiNFdL7Zdr5a_LnXI4SFg2BrEMX8DHLMPKgq8BkIxyvzaILHnt0gkuUAdthjp78bAEbCxlYlnBOVoZXK1Yk91UCS4IT9IltO7m93B7-VFh_KZkfgIWydH84-j0iHg5HUHHV93rliNsEVeT9KTqwMCVMTddP6y8R_LxX0UxbN-WFdQ87N8BgoRKLo.P_fH7BNeuboGo_WLbZ1pfyhlueuhpSDEqrZYfVDE9uE&dib_tag=se&keywords=iphone%2B13&qid=1753009707&sprefix=iphone%2B%2Caps%2C788&sr=8-1&th=1"
USER = "abdurahimhussein292@gmail.com"
header = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
}

PASSWORD = os.environ.get("AMAZON_PASSWORD")

response = requests.get(url=URL, headers=header)
html_response = response.text
soup = BeautifulSoup(html_response, "html.parser")

product_name = soup.select_one("span#productTitle").get_text(strip=True)
price = soup.select_one("span.a-price span.a-offscreen")
price_value = (
    round(float(price.get_text(strip=True).strip("$")), 2)
    if price
    else "Price not found"
)

if price_value < 1000:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=USER, password=PASSWORD)
        connection.sendmail(
            from_addr=USER,
            to_addrs=USER,
            msg=f"Subject:Amazon Price Alert!\n\n{product_name} is now ${price_value}",
        )
        print(f"Email sent! {product_name} is now {price_value}")
