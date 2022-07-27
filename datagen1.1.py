#datagen1.1.py, Colin Maggard, last modified 07/08/22, this program generates data points given statistical parameters
import random,statistics,math,os,sys

reserror = 1000
avgerror = 1000

average = float(input("What is your intended average?: ")) #the average that is intended to be replicated with the data, found roughly 0% error on average in trials
stdev = float(input("What is your intended standard deviation?: ")) #the standard deviation that is intended, found around 2% error on average in trials
points_desired = int(input("How many data points do you need?: ")) #the higher this number, the lower the standard error of the mean
decimal_places = int(input("To what decimal place do you need? (1 is tenths, 2 is hundredths, etc.): ")) #this is for readability and to reduce user rounding
error = float(input("What maximum percent error is permissible?: ")) #this will determine how close the average and standard deviation are to the desired statistical values

stdevplaces = str(stdev)[::-1].find('.') #this finds the amount of decimal places in the intended standard deviation and creates a multiplier
amount = stdev*(10^decimal_places)*(10^(stdevplaces*2))*1.25 #basically this makes it so that the stdev always translates to an integer for the sake of the random function
    
print("\nPoints Created:")
while abs(reserror) >= error or abs(avgerror) >= error:
    numbers = []
    points_created = 0 #this describes how many points have been created so far and is used as a counter
    total = 0 #this is the total amount of points created added together
    differential = 0 #this is the amount that is added to the average to create the new data point; the difference, can be positive or negative
    leftovers = 0 #this is the difference that needs to be made up at some point in order to keep the average constant, imagine it "pulling" the next data points in a certain direction
    while points_created < points_desired:
        
        #this part determines how much the created point differs from the average
        differential = random.randint(-round(amount),round(amount)) #should be roughly around the standard deviation, this creates random but controlled variation
        differential = differential/((10^decimal_places)*(10^(stdevplaces*2))) #back down to whatever decimal place it was supposed to be before, this is to accommodate random function
        differential += leftovers #whatever the current "pull" on the data points in will be factored in in order to sort of force the points to accommodate the average
        
        #this part shows how far off of the average we are and how much we need to balance it out by
        leftovers = leftovers - differential #creates a "pull" in the opposite direction of the difference between the created point and the intended average
        
        #this part creates the created point
        created_point = average + differential
        
        #this part prints the created point and updates the counter and total
        #print(round(created_point,decimal_places)) #rounds to however many decimal places were selected previously
        total += created_point #adds it to a total for certain statistical calculations
        numbers.append(round(created_point,decimal_places)) #adds it to a list for certain statistical calculations
        points_created += 1 #acts as a counter so the correct amount of points can be created

    #statistics section
    avg = statistics.mean(numbers)
    avgerror = 100*round(((avg - average)/average),6)

    res = statistics.pstdev(numbers)
    if stdev != 0:
        reserror = 100*round(((res - stdev)/stdev),6)
    else:
        reserror = 0
        
print(*numbers, sep = "\n")
print("\nCurrent average: " + str(round(avg,6)) + " with percent error " + str(round(avgerror,6)) + "%") #error found to be close to 0% on average in trials
print("Current standard deviation: " + str(round(res,6)) + " with percent error " + str(round(reserror,6)) + "%") #error found to be close to the standard deviation on average in trials

sem = res/(math.sqrt(points_desired))
print("Standard error of the mean: " + str(round(sem,6)))
print("Median: " + str(round(statistics.median(numbers),6)))
print("Range: " + str(min(numbers)) + " to " + str(max(numbers)))
    
print("\nCompleted. Enjoy the data.")

export = input("\nExport to text file (y/n)?: ")
filename = str(input("What would you like to name your text file?: "))
if export == "y":
    with open(os.path.join(sys.path[0], filename), 'w') as fp:
        for item in numbers:
            # write each item on a new line
            fp.write("%s\n" % item) #write each number in the list on a separate line in the text file, can be copied and pasted into a spreadsheet or something
    print('\nDone')