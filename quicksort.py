import csv
import time

f=open("input1.txt")

def quick_sort(my_list):
   quick_sort1(my_list,0,len(my_list)-1)

def quick_sort1(my_list,first,last):
   if first<last:

       splitpoint = partition(my_list,first,last)

       quick_sort1(my_list,first,splitpoint-1)
       quick_sort1(my_list,splitpoint+1,last)


def partition(my_list,first,last):
   pivotvalue = my_list[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and my_list[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while my_list[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = my_list[leftmark]
           my_list[leftmark] = my_list[rightmark]
           my_list[rightmark] = temp

   temp = my_list[first]
   my_list[first] = my_list[rightmark]
   my_list[rightmark] = temp


   return rightmark
   
for my_list in csv.reader(f):
startTime = time.time()
quick_sort(my_list)
elaspedTime- time.time() - startTime
print(elapsedTime)
print(my_list)
#bubble_sort(my_list)
#my_list = [54,26,93,17,77,31,44,55,20,44,15,76,2,96,24,17]
#quick_sort(my_list)
#print(my_list)