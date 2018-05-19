import picamera
import readchar

def main():
    cam = picamera.PiCamera()
    cam.resolution = (640, 480)
    cam.start_preview()

    while True:
        key = readchar.readkey()

        if key == "q":
            break
        elif key == "c":
            for i in range(3):
                fname = "my_picture_{}.png".format(i)
                cam.capture(fname)

    cam.stop_preview()
main()
