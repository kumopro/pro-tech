import wiringpi
import time

led_r_pin = 24
led_g_pin = 18
led_b_pin = 23

# settings
wiringpi.wiringPiSetupGpio()
wiringpi.pinMode(led_r_pin, wiringpi,OUTPUT)
wiringpi.pinMode(led_g_pin, wiringpi,OUTPUT)
wiringpi.pinMode(led_b_pin, wiringpi,OUTPUT)

# main
print("start")
wiringpi.digitalWrite(led_r_pin, wiringpi.HIGH)
wiringpi.digitalWrite(led_g_pin, wiringpi.LOW)
wiringpi.digitalWrite(led_b_pin, wiringpi.LOW)
time.sleep(5)  # [sec]
wiringpi.digitalWrite(led_r_pin, wiringpi.LOW)
wiringpi.digitalWrite(led_g_pin, wiringpi.HIGH)
wiringpi.digitalWrite(led_b_pin, wiringpi.LOW)
time.sleep(5)  # [sec]
wiringpi.digitalWrite(led_r_pin, wiringpi.LOW)
wiringpi.digitalWrite(led_g_pin, wiringpi.LOW)
wiringpi.digitalWrite(led_b_pin, wiringpi.HIGH)
time.sleep(5)  # [sec]
wiringpi.digitalWrite(led_b_pin, wiringpi.LOW)
print("end")
