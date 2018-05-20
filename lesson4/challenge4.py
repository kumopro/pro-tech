def print_name_age(name, age):
    print("Name: " + name)
    print("Age: {}".format(age))

    if age >= 65:
        price = 6700
    elif age >= 18:
        price = 7400
    elif age >= 12:
        price = 6400
    elif age >= 4:
        price = 4800
    else:
        price = 0

    if price > 0:
        print("Price: {}yen".format(price))
    else:
        print("Price: free")


print_name_age("Taro Yamada", 15)
print_name_age("Ai Yamada", 11)
print_name_age("Kenji Yamada", 43)
print_name_age("Sayuri Yamada", 67)
print_name_age("Haru Tanaka", 2)
