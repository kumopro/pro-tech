import readchar

def main():
    while True:
        key = readchar.readkey()
        print(key)

        if key == "q":
            print("quit")
            break

main()
