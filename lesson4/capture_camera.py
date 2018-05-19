import readchar
import picamera

def main():
    cam = picamera.PiCamera()
    cam.resolution = (640, 480)
    cam.start_preview()

    while True:
        key = readchar.readkey()

        if key == "q":
            break
        elif key == "c":
            cam.capture('my_picture.png')

    cam.stop_preview()
main()
