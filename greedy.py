import csv


counter = 0



def min_activities(start_time , end_time , num_act): 
    num_act = num_act
    activities = []
    t = 1
    x = 0
    global counter
   
    
    counter +=1 
    print counter
    
 	
 	
    #This ensures first activity is always selected
    i = 0
    
    activities.insert(0,0)
 
    #Look at each activity and determine if the times overlap with the previous activity
    for j in xrange(num_act):
        
 
 		
        if start_time[j] >= end_time[i]:
            activities.insert(t,j)
            i = j
            t+=1
    
    leng = len(activities)
    
    print activities
    
    #Once a set of activities is added to the list that can occur in the same lecture hall
    #Remove them from the list and repeat above function until no activities remain
    while x < leng:
        start_time.remove(start_time[leng-1])
        end_time.remove(end_time[leng-1])
        leng -= 1

    if len(end_time) > 0:
        min_activities(start_time , end_time, len(end_time))

#Read in the data from text file and add to respective lists.
def main():
    file = open("activities.txt") 
    start_time = []
    end_time = []
    i = 0
    for row in csv.reader(file):
        
        
        if i > 0:
            start_time.append(int(row[0]))
            end_time.append(int(row[1]))
        else:
            num_act = int(row[0])
            i += 1
    
    print(start_time)
    print(end_time)
    print(num_act)
    



	#Call the functions for the program and print the total number of lecture halls 
	#that must be used for the specified activities.
    min_activities(start_time , end_time, num_act)
    print "The lowest numbe of Lecture Halls Used=", counter
    
main()