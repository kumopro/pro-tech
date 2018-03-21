import wiringpi
import time

led_pin = 23

# settings
wiringpi.wiringPiSetupGpio()
wiringpi.pinMode(led_pin, wiringpi,OUTPUT)
wiringpi.softPwmCreate(led_pin, 0, 100)

# main
print("start")
count = 0
brightness = 0
while count < 5:
    while brightness < 100:
        wiringpi.softPwmWrite(led_pin, brightness)
        time.sleep(0.1)  # [sec]
        brightness += 1
    while brightness > 0:
        wiringpi.softPwmWrite(led_pin, brightness)
        time.sleep(0.1)  # [sec]
        brightness -= 1
    count += 1
wiringpi.softPwmWrite(led_pin, 0)
print("end")
