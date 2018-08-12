import csv
import time
f=open("input1.txt")
def bubble_sort(my_list):
    for pass_num in range(len(my_list)-1,0,-1):
        for i in range(pass_num):
            if my_list[i]>my_list[i+1]:
                temp = my_list[i]
                my_list[i] = my_list[i+1]
                my_list[i+1] = temp

#my_list = [54,26,93,17,77,31,44,55,20]
for my_list in csv.reader(f):
startTime = time.time()
buble_sort(my_list)
elapsedTime = time.time() - startTime
print(elapsedTime)
print(my_list)
#bubble_sort(my_list)
#print(my_list)