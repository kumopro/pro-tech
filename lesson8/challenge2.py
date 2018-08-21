import requests
import json
import wiringpi
import time

def get_tomorrow_temp_diff():
    url = 'http://weather.livedoor.com/forecast/webservice/json/v1?city=130010'
    data = requests.get(url).json()

    forecasts = data['forecasts']
    tomorrow_forecast = forecasts[1]

    temp = tomorrow_forecast['temperature']
    min_temp = temp['min']['celsius']
    max_temp = temp['max']['celsius']

    return max_temp - min_temp

def main():    
    led_pin = 23
    wiringpi.wiringPiSetupGpio()
    wiringpi.pinMode(led_pin, wiringpi.OUTPUT)

    diff = get_tomorrow_temp_diff()

    if diff > 10:
        print('明日は1日の間に気温差が10度以上あります')
        wiringpi.digitalWrite(led_pin, wiringpi.HIGH)
        time.sleep(5)
        wiringpi.digitalWrite(led_pin, wiringpi.LOW)        

main()
