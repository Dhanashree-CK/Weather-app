import requests
from config import API_KEY

BASE_URL = "https://api.openweathermap.org/data/2.5/"

def get_current_weather(city):
    url = f"{BASE_URL}weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url).json()
    
    if response.get("cod") != 200:
        return None
    
    return {
        "city": response["name"],
        "temperature": response["main"]["temp"],
        "humidity": response["main"]["humidity"],
        "condition": response["weather"][0]["description"].title(),
        "icon": response["weather"][0]["icon"]
    }

def get_forecast_5days(city):
    url = f"{BASE_URL}forecast?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url).json()

    forecast = []
    if response.get("cod") != "200":
        return forecast

    # pick one reading per day (12:00 pm)
    for item in response["list"]:
        if "12:00:00" in item["dt_txt"]:
            forecast.append({
                "date": item["dt_txt"].split(" ")[0],
                "temperature": item["main"]["temp"],
                "humidity": item["main"]["humidity"],
                "condition": item["weather"][0]["description"].title(),
                "icon": item["weather"][0]["icon"]
            })
    return forecast

weather.py
