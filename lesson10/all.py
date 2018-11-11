import wiringpi
import time
import picamera
from watson_developer_cloud import VisualRecognitionV3
from watson_developer_cloud import LanguageTranslatorV3
from watson_developer_cloud import TextToSpeechV1
import json
import pygame.mixer

def translate(text_en):
    version = '2018-05-01'
    api_key = 'FcHA3xI6U7H2QaTQ9jiwwkNvWRgmwIK_VgkTeB6HjFSF'

    translator = LanguageTranslatorV3(version=version, iam_apikey=api_key)

    results = translator.translate(text=text_en, model_id='en-ja').get_result()
    return results['translations']['translation']

def text2speech(text, filename):
    username = '4a3d1e76-9132-4f83-b131-122da190f921'
    password = 'QmHSjNTK52jt'

    text_to_speech = TextToSpeechV1(username=username, password=password)
    r = text_to_speech.synthesize(text, 'audio/mp3', 'ja-JP_EmiVoice').get_result().content

    with open(filename, 'wb') as audio_file:
        audio_file.write(r)

def play(filename):
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    time.sleep(1)
    pygame.mixer.music.stop()
    pygame.mixer.quit()

def main():
    trig_pin = 17
    echo_pin = 27

    wiringpi.wiringPiSetupGpio()
    wiringpi.pinMode(trig_pin, wiringpi.OUTPUT)
    wiringpi.pinMode(echo_pin, wiringpi.INPUT)

    wiringpi.digitalWrite(trig_pin, wiringpi.LOW)

    cam = picamera.PiCamera()
    cam.resolution = (640, 480)
    cam.start_preview()
    img_filename = 'my_picture.png'
    audio_filename = 'speech_result.mp3'

    while True:
        distance = getDistance(trig_pin, echo_pin)
        print(distance)

        time.sleep(0.5)  # [sec]

        if distance < 15:
            print('capture')
            cam.capture(img_filename)
            result_en = recognize(img_filename)
            print(result_en)
            result_ja = translate(result_en)
            print(result_ja)
            text2speech(result_ja, audio_filename)
            time.sleep(1)
            play(audio_filename)
        if distance < 8:
            break

    cam.stop_preview()

main()
