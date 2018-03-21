import wiringpi
import time

led_pin = 23

# settings
wiringpi.wiringPiSetupGpio()
wiringpi.pinMode(led_pin, wiringpi.OUTPUT)

# main
print("start")
wiringpi.digitalWrite(led_pin, wiringpi.HIGH)
time.sleep(5)  # [sec]
wiringpi.digitalWrite(led_pin, wiringpi.LOW)
print("end")
