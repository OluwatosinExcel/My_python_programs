# This program helps users get weather information from their specified location.
import requests
from pprint import pprint

API_Key = 'db53c569d4657d69db0a8d95d8027d12'

city = input("Enter a City: ")

base_url = "http://api.openweathermap.org/data/2.5/weather?appid="+API_Key+"&q="+city

weather_data = requests.get(base_url).json()

pprint(weather_data)
print("A detailed information on " + city + " weather.")

