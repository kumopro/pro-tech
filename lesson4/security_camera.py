import cv2
import readchar

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

    cap = cv2.VideoCapture(0)
    cap.set(CV_CAP_PROP_FRAME_WIDTH, 640)
    cap.set(CV_CAP_PROP_FRAME_HEIGHT, 400)

    while True:
        distance = getDistance(trig_pin, echo_pin)
        print(distance)

        time.sleep(2)  # [sec]

        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("Capture", gray)
        key = readchar.readkey()

        if key == "q":
            break
        elif key == "c" or distance < 15:
            cv2.imwrite("image.png", gray)

    cap.release()
    cv2.destroyAllWindows()

main()
