import csv
import time
#Uncomment to use a text file for input.
#f=open("input1.txt")
my_list = [2,1,0,8,9,3,0,0]
my_list2 = [[7,6,6,9,9,7,8],
			[8,9,5,3,2,7,9],
			[7,6,5,6,6,6,3],
			[3,3,2,5,9,1,4]]
			
def bubble_sort(my_list):
    for pass_num in range(len(my_list)-1,0,-1):
        for i in range(pass_num):
            if my_list[i]>my_list[i+1]:
                temp = my_list[i]
                my_list[i] = my_list[i+1]
                my_list[i+1] = temp



#for my_list in csv.reader(f):

startTime = time.time()
bubble_sort(my_list)
elapsedTime = time.time() - startTime
print(elapsedTime)
print(my_list)
for my_list in my_list2:
	startTime = time.time()
	bubble_sort(my_list)
	elapsedTime = time.time() - startTime
	print(my_list)
print(elapsedTime)