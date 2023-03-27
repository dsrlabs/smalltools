# Weather App 
# Get Your Free API : http://openweathermap.org/appid
# pip install requests
import requests
from bs4 import BeautifulSoup as bs
def get_weather(loc):
    # Set API
    key = "c710c77ddcb3d7f2f42f7c04d48e4f90"
    api_url = f"http://api.openweathermap.org/data/2.5/weather?"
    params = f"q={loc}&appid={key}"
    
    # Get the response from the API
    url = api_url + params
    response = requests.get(url)
    weather = response.json()
# Fetch Weather
    print(f"Weather for {loc}:")
    temp = weather['main']['temp']
    print("Temperature:", temp - 273.15, "Celsius")
    humidity = weather['main']['humidity']
    print("Humidity:", humidity, "%")
    wind = weather['wind']['speed']
    print("Wind speed:", wind, "m/s")
# main
get_weather('Bowie')