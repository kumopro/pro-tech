import requests
import json
import wiringpi
import time

def print_tomorrow_temp():
    url = 'http://weather.livedoor.com/forecast/webservice/json/v1?city=130010'
    data = requests.get(url).json()

    forecasts = data['forecasts']
    tomorrow_forecast = forecasts[1]
    temp = tomorrow_forecast['temperature']
    print(temp)
    
def get_tomorrow_weather():
    url = 'http://weather.livedoor.com/forecast/webservice/json/v1?city=130010'
    data = requests.get(url).json()

    forecasts = data['forecasts']
    tomorrow_forecast = forecasts[1]
    tomorrow_weather = tomorrow_forecast['telop']
    print(tomorrow_weather)

    return tomorrow_weather

def main():    
    print_tomorrow_temp()

main()
