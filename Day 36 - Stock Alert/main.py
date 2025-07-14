import requests
import datetime as dt
import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
from_number = os.getenv("TWILIO_PHONE_NUMBER")
to_number = os.getenv("MY_PHONE_NUMBER")

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

API_ENDPOINT_STOCK = "https://www.alphavantage.co/query"
API_KEY_ST = "QGJWAWA4MLUM69K1"

API_ENDPOINT_NEWS = "https://newsapi.org/v2/everything"
API_KEY_NEWS = "036d0a88b37d4122b56c1952bdc07495"
params = {"symbol": STOCK, "function": "TIME_SERIES_DAILY", "apikey": API_KEY_ST}

response = requests.get(url=API_ENDPOINT_STOCK, params=params)
data = response.json()
try:
    dates = sorted(data["Time Series (Daily)"].keys(), reverse=True)
    latest_day = dates[0]
    previous_day = dates[1]

    yesterday_stock_price = float(data["Time Series (Daily)"][latest_day]["4. close"])
    previous_stock_price = float(data["Time Series (Daily)"][previous_day]["4. close"])

    diff = yesterday_stock_price - previous_stock_price
    percentage_diff = round((diff / previous_stock_price) * 100, 1)
    arrow = "🔺" if diff > 0 else "🔻"
except (KeyError, IndexError, ValueError) as e:
    print(f"Failed to extract stock prices: {e}")
    exit()

if abs(percentage_diff) > 1:
    new_params = {
        "apiKey": API_KEY_NEWS,
        "q": COMPANY_NAME,
    }
    try:
        response_news = requests.get(url=API_ENDPOINT_NEWS, params=new_params)
        response_news.raise_for_status()
    except requests.RequestException as e:
        print(f"Failed to fetch news: {e}")
        exit()

    news_data = response_news.json()
    articles = news_data["articles"][:1]  # Get the top 3 articles
    if not articles:
        print("No news articles found.")
        exit()
    news = []
    for article in articles:
        news.append({"headline": article["title"], "Brief": article["description"]})

    client = Client(account_sid, auth_token)
    for each_news in news:
        message = client.messages.create(
            body=f"{STOCK}: {arrow}{percentage_diff}%\nHeadline: {each_news['headline']}\nBrief: {each_news['Brief']}",
            from_=from_number,
            to=to_number,
        )
        print("Sent message:", message.body)
