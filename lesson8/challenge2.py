import requests
import json
import wiringpi
import time

def get_min_temp_diff():
    url = 'http://weather.livedoor.com/forecast/webservice/json/v1?city=130010'
    data = requests.get(url).json()

    forecasts = data['forecasts']
    today_forecast = forecasts[0]
    tomorrow_forecast = forecasts[1]

    today_temp = today_forecast['temperature']
    today_min_temp = today_temp['min']['celsius']

    tomorrow_temp = tomorrow_forecast['temperature']
    tomorrow_min_temp = tomorrow_temp['min']['celsius']

    return tomorrow_min_temp - today_min_temp

def main():    
    led_pin = 23
    wiringpi.wiringPiSetupGpio()
    wiringpi.pinMode(led_pin, wiringpi.OUTPUT)

    diff = get_min_temp_diff()

    if diff < 0:
        print('明日の朝は今日より冷え込みます')
        wiringpi.digitalWrite(led_pin, wiringpi.HIGH)
        time.sleep(5)
        wiringpi.digitalWrite(led_pin, wiringpi.LOW)        

main()
