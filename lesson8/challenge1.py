import requests
import json

def print_tomorrow_temp():
    url = 'http://weather.livedoor.com/forecast/webservice/json/v1?city=130010'
    data = requests.get(url).json()

    forecasts = data['forecasts']
    tomorrow_forecast = forecasts[1]
    temp = tomorrow_forecast['temperature']
    min_temp = temp['min']['celsius']
    max_temp = temp['max']['celsius']
    print("明日の最低気温は{}度です".format(min_temp))
    print("明日の最高気温は{}度です".format(max_temp))
    
def main():    
    print_tomorrow_temp()

main()
