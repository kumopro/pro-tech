import requests
import json
import wiringpi
import time
from watson_developer_cloud import TextToSpeechV1
import pygame.mixer

def get_forecast():
    url = 'http://weather.livedoor.com/forecast/webservice/json/v1?city=130010'
    data = requests.get(url).json()

    location = data['location']['city']
    forecasts = data['forecasts']
    tomorrow_forecast = forecasts[1]
    tomorrow_weather = tomorrow_forecast['telop']

    forecast = '明日の{0}の天気は{1}です'.format(location, tomorrow_weather)

    return forecast

def text2speech(text, filename):
    api_key = ''
    url = 'https://stream.watsonplatform.net/text-to-speech/api'

    text_to_speech = TextToSpeechV1(iam_apikey=api_key, url=url)
    r = text_to_speech.synthesize(text, 'audio/mp3', 'ja-JP_EmiVoice').get_result().content

    with open(filename, 'wb') as audio_file:
        audio_file.write(r)

def play(filename):
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    time.sleep(5)
    pygame.mixer.music.stop()
    pygame.mixer.quit()

def getDistance(trig_pin, echo_pin):
    ### trigger
    wiringpi.digitalWrite(trig_pin, wiringpi.HIGH)
    time.sleep(0.00001)  # [sec]
    wiringpi.digitalWrite(trig_pin, wiringpi.LOW)

    ### response time
    while wiringpi.digitalRead(echo_pin) == 0:
        time_begin = time.time()
    
    while wiringpi.digitalRead(echo_pin) == 1:
        time_end = time.time()

    t = time_end - time_begin
    
    ### calculate distance
    distance = t * 17000

    return distance

def save_forecast_audio(forecast_filename):
    forecast = get_forecast()  # forecastは英語で「予報」という意味
    print(forecast)

    text2speech(forecast, forecast_filename)

def main():
    trig_pin = 17
    echo_pin = 27

    wiringpi.wiringPiSetupGpio()
    wiringpi.pinMode(trig_pin, wiringpi.OUTPUT)
    wiringpi.pinMode(echo_pin, wiringpi.INPUT)

    wiringpi.digitalWrite(trig_pin, wiringpi.LOW)
    forecast_filename = 'forecast.mp3'

    while True:
        distance = getDistance(trig_pin, echo_pin)
        print(distance)

        time.sleep(0.5)  # [sec]

        if distance < 15:
            save_forecast_audio(forecast_filename)
            time.sleep(1)
            play(forecast_filename)
        if distance < 8:
            break

main()
