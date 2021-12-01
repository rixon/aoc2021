#!/opt/local/bin/python

f = open('1a.txt', 'r')
l = []

for n in f:
    l.append(int(n))

f.closed

last = 0
count = 0

for n in l:
  #print(n)
  if not last == 0:
    if n > last:
      count += 1
      #print("greater")
  #else:
  #  print("Skipped first")
  last = n

print(count)

