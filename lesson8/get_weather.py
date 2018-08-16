import requests
import json

def main():
    url = 'http://weather.livedoor.com/forecast/webservice/json/v1?city=130010'
    data = requests.get(url).json()
    print(data)
    
main()
