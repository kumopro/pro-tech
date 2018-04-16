def countup(num):
    count = 1
    while count <= num:
        if count % 3 == 0:
            print(count)
        count += 1

countup(10)
