import csv
import os

#creates the path to read the csv file and outputs 
# that file onto a txt file in the analysis folder
file_to_load = os.path.join("Resources", "election_data.csv")
file_to_output = os.path.join("Analysis", "election_analysis.txt")

#defines all of my variables, put the names as variables to more easily input in the code
totalvotes=0
charles="Charles Casper Stockham"
charles_votes=0
diana="Diana DeGette"
diana_votes=0
raymon="Raymon Anthony Doane"
raymon_votes=0
#create a result dictionary that will store the results and the corresponding candidate
results={}
#creates a list that will be used decide which candidate had the highest share of the votes
shares=[]

#first open which loops through the code and counts the total number of votes along with the votes for charles, skip header
with open(file_to_load) as file:
    rows = csv.reader(file,delimiter=",")
    header = next(rows)

    for row in rows:
        #for each row it adds one to the total vote counter
        totalvotes+=1
        #each time the value of column 3 is equal to charles name then it is added to the charles vote counter
        if row[2]==charles:
            charles_votes+=1
    #multiplies times 100 to put the share into percentage
    charles_share=(charles_votes/totalvotes)*100
    #append dictionary and list which will be used to 
    results[charles_share]=charles
    shares.append(charles_share)

#second open loop through the code to count the votes for diana, total is not needed to be counted as it is assigned already
# to not be repetitive in my comments, all of the functions completed for charles above are duplicated for Diana and Raymon    
with open(file_to_load) as file:
    rows = csv.reader(file,delimiter=",")
    header = next(rows)

    for row in rows:
        
        if row[2]==diana:
            diana_votes+=1

    diana_share=(diana_votes/totalvotes)*100
    results[diana_share]=diana
    shares.append(diana_share)

with open(file_to_load) as file:
    rows = csv.reader(file,delimiter=",")
    header = next(rows)

    for row in rows:
        
        if row[2]==raymon:
            raymon_votes+=1
        
    raymon_share=(raymon_votes/totalvotes)*100
    results[raymon_share]=raymon
    shares.append(raymon_share)

#finds the highest share of votes
highestvote=max(shares)

#uses the result above to find the corresponding key (candidate name) to find the winner
winner=results[highestvote]

#print(f"{winner}"), line was used to test code
#print results below, 3f was used to insert 3 decimal values as presented in the example
output=f"""
Election Results
-------------------------
Total Votes: {totalvotes}
-------------------------
Charles Casper Stockham: {charles_share:.3f}% ({charles_votes})
Diana DeGette: {diana_share:.3f}% ({diana_votes})
Raymon Anthony Doane: {raymon_share:.3f}% ({raymon_votes})
-------------------------
Winner: {winner}
-------------------------
"""
#prints results into the terminal
print(output)

#prints the resutls into a txt file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)