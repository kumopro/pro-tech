import wiringpi
import time
import picamera
from watson_developer_cloud import VisualRecognitionV3
import json

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

def recognize(filename):
    version = '2018-03-19'
    api_key = ''

    recognizer = VisualRecognitionV3(version=version, iam_apikey=api_key)
    with open(filename, 'rb') as image:
        results = recognizer.classify(image).get_result()
    r = results['images'][0]['classifiers'][0]['classes']
    return r[0]['class']

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
    filename = 'my_picture.png'

    while True:
        distance = getDistance(trig_pin, echo_pin)
        print(distance)

        time.sleep(0.5)  # [sec]

        if distance < 15:
            print('capture')
            cam.capture(filename)
            result = recognize(filename)
            print(result)
        if distance < 8:
            break

    cam.stop_preview()

main()
