import wiringpi
import time

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
    count = 0
    body_up = False

    print('腹筋スタート！')

    start_time = time.time()
    current_time = time.time()

    while (current_time - start_time) < 10:  # 10秒間カウント
        distance = getDistance(trig_pin, echo_pin)

        time.sleep(0.5)  # [sec]

        if distance < 8 and body_up == False:
            count += 1
            body_up = True
            print('count: {}'.format(count))
        if distance > 20 and body_up == True:
            body_up = False

        current_time = time.time()

    print('腹筋回数：{}回'.format(count))
    print('お疲れ様でした！')

main()
