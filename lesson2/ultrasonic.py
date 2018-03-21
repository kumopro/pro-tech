import wiringpi
import time

trig_pin = 17
echo_pin = 27

# settings
wiringpi.wiringPiSetupGpio()
wiringpi.pinMode(trig_pin, wiringpi.OUTPUT)
wiringpi.pinMode(echo_pin, wiringpi.INPUT)

wiringpi.digitalWrite(trig_pin, wiringpi.LOW)

# main
print("start")
while True:
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
    distance = 
    print(distance)

    time.sleep(1)  # [sec]
print("end")
