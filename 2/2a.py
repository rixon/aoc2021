#!/opt/local/bin/python3

directions = open("2.txt", "r")
h = 0
v = 0

for direction in directions:
    udf, mag = direction.split(" ")
    if udf == "forward":
        h += int(mag)
    else:
        if udf == "up":
            v -= int(mag)
        elif udf == "down":
            v += int(mag)
        else:
            print("Unexpected direction " + udf)

print("h = " + str(h) + ", v = " + str(v) + ", combined = " + str(v * h))
