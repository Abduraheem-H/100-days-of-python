import requests
from bearerAuth import BearerAuth
import datetime as dt
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")
BEARER_TOKEN = os.getenv("BEARER_TOKEN")

API_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
API_SHEET_ENDPOINT = (
    "https://api.sheety.co/90ca9e077fda5b067e514690ed5d8a1f/myWorkouts/workouts"
)

# User input
exercise_input = input("Tell me which exercises you did: ")

# Request headers and body for Nutritionix
headers = {"x-app-id": APP_ID, "x-app-key": API_KEY, "Content-Type": "application/json"}

payload = {
    "query": exercise_input,
    "gender": "male",
    "weight_kg": 70,
    "height_cm": 182,
    "age": 22,
}


response = requests.post(url=API_ENDPOINT, json=payload, headers=headers)
exercise_data = response.json().get("exercises", [])
print("Exercise Data:", exercise_data)

now = dt.datetime.now()
date_today = now.strftime("%Y/%m/%d")
time_now = now.strftime("%H:%M:%S")


for workout in exercise_data:
    data = {
        "workout": {
            "date": date_today,
            "time": time_now,
            "exercise": workout["name"].title(),
            "duration": round(workout["duration_min"], 1),
            "calories": round(workout["nf_calories"], 1),
        }
    }
    print("Logging to Sheet:", data)  # Debugging line

    res = requests.post(
        url=API_SHEET_ENDPOINT, auth=BearerAuth(BEARER_TOKEN), json=data
    )
    if res.status_code == 200:
        print("Successfully logged the workout.")
    else:
        print(f"Failed to log the workout. Status code: {res.status_code}")
