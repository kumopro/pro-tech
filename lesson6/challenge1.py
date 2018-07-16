import picamera

def main():
    cam = picamera.PiCamera()
    cam.resolution = (640, 480)
    cam.start_preview()
    fname = "my_picture.png"
    cam.capture(fname)
    cam.stop_preview()

main()
