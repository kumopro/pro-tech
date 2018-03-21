import wiringpi
import time

led_pin = 23

# settings
wiringpi.wiringPiSetupGpio()
wiringpi.pinMode(led_pin, wiringpi.OUTPUT)

# main
print("start")
wiringpi.softPwmCreate(led_pin, 0, 100)
wiringpi.softPwmWrite(led_pin, 20)
time.sleep(5)  # [sec]
wiringpi.softPwmWrite(led_pin, 0)
print("end")
