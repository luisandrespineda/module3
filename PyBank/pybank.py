#imports necessary modules
import csv
import os

#sets file path to read files from and txt files to put
file_to_load = os.path.join("Resources", "budget_data.csv")
file_to_output = os.path.join("Analysis", "budget_analysis.txt")

#sets the variables that will be used throughout the code
totalmonth=0
totalprofit=0
totalchange=0
changeinmonths=0
previousprofit=0
greatestincrease=0
greatestincreasemonth=0
greatestdecreasemonth=0
#creates a list in which the change results will be stored, this will be used to find the max increase and decrease
changelist=[]

#open and reads csv files
with open(file_to_load) as file:
    rows = csv.reader(file)
    header = next(rows)

    #skips the header and jan files    
    jan_row =next(rows)
    
    #adds to the total month with each iteration and the value from column 2 with each iteration
    totalmonth +=1
    totalprofit += int(jan_row[1])

    previousprofit = int(jan_row[1])

    for row in rows:
        totalmonth +=1
        totalprofit += int(row[1]) 

        currentprofit=int(row[1])
        change= currentprofit - previousprofit
        changeinmonths += 1
        totalchange += change #adds each change to the total change

        changelist.append(change) # adds each change to the list, used for finding max
        previousprofit=currentprofit #sets a new previous profit to compare against

        #use python command to find the max increase and decrease
        maxincrease=max(changelist)
        maxdecrease=min(changelist)

        #adds one to the indeces in order to skip the header row
        maxincindex=changelist.index(maxincrease)+1
        maxdecindex=changelist.index(maxdecrease)+1

#the following two clusters of code are used to pull the maximum increase and maximum decrease
with open(file_to_load) as file:
        rows = csv.reader(file)
        next(rows) 

        #I used the index of the max increase to pul the date from the original csv column, the same approach was used for the min
        counter = 0
        maxincdate = None
        for row in rows:
            if counter == maxincindex:
                maxincdate = row[0]
                break
            counter += 1

with open(file_to_load) as file:
        rows = csv.reader(file)
        next(rows) 

        counter = 0
        maxdecdate = None
        for row in rows:
            if counter == maxdecindex:
                maxdecdate = row[0]
                break
            counter += 1
#print(f"{maxdecdate}"), print command was used to test the code

output=f"""
Financial Analysis
----------------------------
Total Months: {totalmonth}
Total: ${totalprofit}
Average Change: ${totalchange/changeinmonths:.2f}
Greatest Increase in Profits: {maxincdate} (${maxincrease})
Greatest Decrease in Profits: {maxdecdate} (${maxdecrease})
"""
#print output into termina
print(output)

#print output into the next txt file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)