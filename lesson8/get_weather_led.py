import requests
import json

def get_tomorrow_weather():
    url = 'http://weather.livedoor.com/forecast/webservice/json/v1?city=130010'
    data = requests.get(url).json()

    forecasts = data['forecasts']
    forecast_tomorrow = forecasts[1]
    weather_tomorrow = forecast_tomorrow['telop']
    print(weather_tomorrow)
    
    return weather_tomorrow

def main():
    led_pin = 23
    wiringpi.wiringPiSetupGpio()
    wiringpi.pinMode(led_pin, wiringpi.OUTPUT)

    if 'é' in weather_tomorrow:
        print('ææはéがéります')
        wiringpi.digitalWrite(led_pin, wiringpi.HIGH)
    else:
        print('ææはéがéりません')
        wiringpi.digitalWrite(led_pin, wiringpi.LOW)

main()
