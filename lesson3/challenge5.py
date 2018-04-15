import wiringpi
import time


def led_blink(led_pin):
    wiringpi.digitalWrite(led_pin, wiringpi.HIGH)
    time.sleep(0.5)  # [sec]
    wiringpi.digitalWrite(led_pin, wiringpi.LOW)


def getUltrasonicDistance(trig_pin, echo_pin):
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
    led_pin = 23

    wiringpi.wiringPiSetupGpio()
    wiringpi.pinMode(trig_pin, wiringpi.OUTPUT)
    wiringpi.pinMode(echo_pin, wiringpi.INPUT)
    wiringpi.pinMode(led_pin, wiringpi.OUTPUT)

    wiringpi.digitalWrite(trig_pin, wiringpi.LOW)

    print("start")
    while True:
        distance = getUltrasonicDistance(trig_pin, echo_pin)
        print(distance)
        
        if distance < 10:
            led_blink(led_pin)

        time.sleep(1)  # [sec]
    print("end")

main()
