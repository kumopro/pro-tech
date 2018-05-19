import readchar

def main():
    while True:
        key = readchar.readkey()

        if key:
            print(key)

        if key == "q":
            print("quit")
            break

main()
