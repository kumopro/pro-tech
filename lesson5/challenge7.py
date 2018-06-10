for i in range(0, 180, 20):
    hour = int(i / 60)
    min = i - 60 * hour
    print("{0:02d}:{1:02d}".format(hour, min))
