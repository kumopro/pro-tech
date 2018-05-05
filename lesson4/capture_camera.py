import picamera
import readchar

def main():
    cam = picamera.PiCamera()
    cam.resolution = (640, 480)
    camera.start_preview()

    while True:
        key = readchar.readkey()

        if key == "q":
            break
        elif key == "c":
            camera.capture('my_picture.png')

    camera.stop_preview()
main()
