#datapoints test, Colin Maggard, last modified 06/10/22, this uses outdated variable names and export functionality does not work
#that being said, the statistical functionality is the same as the most recent version
#this program tests the accuracy of the program by determining average error for mean and stdev over 100 trials of various sample sizes
import random,statistics,math

created = 0 #this describes how many points have been created so far
total = 0 #this is the total amount of points created added up
differential = 0 #this is the amount that is added to the average
leftovers = 0 #this is the difference that needs to be made up at some point in order to keep the average constant
trials = 100
completed = 0
samplesize = 1
tests = 4
finished = 0

numbers = [] #each number is stored in this list primarily to determine standard deviation
averages = []
stdevs = []

average = float(input("What is your intended average?: "))
stdev = float(input("What is your intended standard deviation?: "))
divisible = 2

#this part finds the amount of decimal places in the intended standard deviation
stdevplaces = str(stdev)[::-1].find('.')
#print("\nAmount of decimal places in standard deviation: " + str(stdevplaces))


multiplier = 1.25

amount = stdev*(10^divisible)*(10^(stdevplaces*2))*multiplier #basically this makes it so that the stdev always translates to an integer
#print(amount)

while finished < tests:
    while completed < trials:
        while created < samplesize:
            
            #this part determines how much the created point differs from the average
            differential = random.randint(-round(amount),round(amount)) #should be roughly around the standard deviation
            differential = differential/((10^divisible)*(10^(stdevplaces*2))) #makes it back down to whatever decimal place it was supposed to be
            differential += leftovers
            
            #this part shows how far off of the average we are and how much we need to balance it out by
            leftovers = leftovers - differential
            
            #this part creates the created point
            created_point = average + differential
            
            #this part prints the created point and updates the counter and total
            total += created_point
            numbers.append(round(created_point,divisible))
            created += 1


        #statistics section
        avg = statistics.mean(numbers)
        avgerror = 100*round(((avg - average)/average),6)
        #print("\nCurrent average: " + str(round(avg,6)) + " with percent error " + str(avgerror) + "%")
        averages.append(avgerror)
        res = statistics.pstdev(numbers)
        reserror = 100*round(((res - stdev)/stdev),6)
        stdevs.append(round(res,6))
        #print("Current standard deviation: " + str(round(res,6)) + " with percent error " + str(reserror) + "%")
        completed += 1
        
        numbers = []
        created = 0
        differential = 0
        leftovers = 0
        total = 0
    
    
        print("\nFor sample size of " + str(samplesize) + ":")
        print("Average average percent error: " + str(statistics.mean(averages)))
        print("Average stdev percent error: " + str(statistics.mean(stdevs)))
        
        averages = []
        stdevs = []
    
    
        samplesize = samplesize * 10
        
    finished += 1
    
print("\nCompleted. Enjoy the data.")