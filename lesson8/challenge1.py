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
    min_temp = temp['min']['celcius']
    max_temp = temp['max']['celcius']
    print("ææのæäææは{}åです".format(min_temp))
    print("ææのæéææは{}åです".format(max_temp))
    
def main():    
    print_tomorrow_temp()

main()
