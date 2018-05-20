import wiringpi
import picamera

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

    while True:
        distance = getDistance(trig_pin, echo_pin)
        print(distance)

        time.sleep(2)  # [sec]

        if distance < 15:
            print("capture")
            fname = "my_picture.png"
            cam.capture(fname)
        elif distance < 8:
            break

    cam.stop_preview()

main()
