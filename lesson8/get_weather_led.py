import requests
import json
import wiringpi

def get_tomorrow_weather():
    url = 'http://weather.livedoor.com/forecast/webservice/json/v1?city=130010'
    data = requests.get(url).json()

    forecasts = data['forecasts']
    tomorrow_forecast = forecasts[1]
    tomorrow_weather = forecast_tomorrow['telop']
    print(tomorrow_weather)
    return tomorrow_weather

def main():    
    led_pin = 23
    wiringpi.wiringPiSetupGpio()
    wiringpi.pinMode(led_pin, wiringpi.OUTPUT)
    
    tomorrow_weather = get_tomorrow_weather

    if '雨' in tomorrow_weather:
        print('明日は雨が降ります')
        wiringpi.digitalWrite(led_pin, wiringpi.HIGH)
    else:
        print('明日は雨が降りません')
        wiringpi.digitalWrite(led_pin, wiringpi.LOW)

main()
