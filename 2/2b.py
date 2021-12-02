#!/opt/local/bin/python3

directions = open("2.txt", "r")
h = 0
depth = 0
aim = 0

for direction in directions:
    udf, mag = direction.split(" ")
    if udf == "forward":
        h += int(mag)
        depth += aim * int(mag)
    else:
        if udf == "up":
            aim -= int(mag)
        elif udf == "down":
            aim += int(mag)
        else:
            print("Unexpected direction " + udf)

print("h = " + str(h) + ", depth = " + str(depth) + ", aim = " + str(aim) + ", combined = " + str(depth * h))
