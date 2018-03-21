import wiringpi
import time

led_pin = 23

# settings
wiringpi.wiringPiSetupGpio()
wiringpi.pinMode(led_pin, wiringpi,OUTPUT)
wiringpi.softPwmCreate(led_pin, 0, 100)

# main
print("start")
brightness = 0
while brightness <= 100:
    wiringpi.softPwmWrite(led_pin, brightness)
    time.sleep(0.5)  # [sec]
    brightness += 1
wiringpi.softPwmWrite(led_pin, 0)
print("end")
