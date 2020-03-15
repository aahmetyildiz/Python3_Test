from datetime import datetime




for i in range(16):
    print(str(i))



for x in "banana":

    if x == "a":
        continue

    print(x)




for x in "banana":

    if x == "n":
        break

    print(x)



second = datetime.now().second
while second:

    second = datetime.now().second
    if second > 50:

        if second == 54:
            continue

        print(second)

    else:
        break

