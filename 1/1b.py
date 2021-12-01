#!/opt/local/bin/python3

f = open('1a.txt', 'r')
l = []

for n in f:
    l.append(int(n))

f.closed

a = 0
b = 0
c = 0
count = 0
primed = False

for n in l:
  #print(n)
  if primed:
    print(n + a + b, end='')
    if n + a + b > a + b + c:
      count += 1
      print("greater", end='')
    print()
  else:
    print("not primed", end='')
    print(n + a + b)
    c = b
    b = a
    a = n
    if (a != 0) and (b != 0) and (c != 0):
      primed = True
  c = b
  b = a
  a = n

# errata: subtract one!
print(int(count)-1)

