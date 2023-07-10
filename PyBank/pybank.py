import csv
import os

file_to_load = os.path.join("Resources", "budget_data.csv")
file_to_output = os.path.join("Analysis", "budget_analysis.txt")

totalmonth=0
totalprofit=0
totalchange=0
changeinmonths=0
previousprofit=0
greatestincrease=0
greatestincreasemonth=0
greatestdecreasemonth=0
changelist=[]

with open(file_to_load) as file:
    rows = csv.reader(file)
    header = next(rows)
    
    jan_row =next(rows)
    
    totalmonth +=1
    totalprofit += int(jan_row[1])

    previousprofit = int(jan_row[1])

    for row in rows:
        totalmonth +=1
        totalprofit += int(row[1]) 

        currentprofit=int(row[1])
        change= currentprofit - previousprofit
        changeinmonths += 1
        totalchange += change

        changelist.append(change)
        previousprofit=currentprofit #sets a new previous profit to compare against


        maxincrease=max(changelist)
        maxdecrease=min(changelist)

        #adds one to the indeces in order to skip the header row
        maxincindex=changelist.index(maxincrease)+1
        maxdecindex=changelist.index(maxdecrease)+1

# I pulled the index 
with open(file_to_load) as file:
        rows = csv.reader(file)
        next(rows) 

        counter = 0
        maxincdate = None
        for row in rows:
            if counter == maxincindex:
                maxincdate = row[0]
                break
            counter += 1
    #if a change is > than the previous increase then pull the row [0] value to 

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
    #if a change is > than the previous increase then pull the row [0] value to 
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

print(output)

with open(file_to_output, "w") as txt_file:
    txt_file.write(output)