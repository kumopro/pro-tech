import wiringpi
import time

def main():
    led_pin = 17

    # settings
    wiringpi.wiringPiSetupGpio()
    wiringpi.pinMode(led_pin, wiringpi.OUTPUT)

    # main
    print("start")
    wiringpi.digitalWrite(led_pin, wiringpi.HIGH)
    time.sleep(5)  # [sec]
    wiringpi.digitalWrite(led_pin, wiringpi.LOW)
    print("end")

main()
