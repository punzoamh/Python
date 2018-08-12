import csv
f=open("input1.txt")
for row in csv.reader(f):
    print(row)
length = (len(row))
sum = 0
while length > 0:
    sum = sum + int(row[length - 1])
    length -= 1
print(sum)