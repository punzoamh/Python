import csv
f=open("input2.txt")
total = 0
for row in csv.reader(f):
    length = (len(row))
    print(row)
    while length > 0:
        total = total + int(row[length - 1])
        print(total)
        length -= 1
print(total)