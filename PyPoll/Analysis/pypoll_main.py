#importing modules needed
import csv

# define file path
csvpath = '/Users/brennancurrie/Desktop/My_Code/Class_Materials/Challenges/Brennan_Currie_Module_3_Challenge/python_challenge/PyPoll/Resources/election_data.csv'

#open csv
with open(csvpath) as csvfile:

    #read csv/specify delimiter
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)
    
    #read the header first row
    csvheader = next(csvreader)

    
    #rows & loop
    votecount = 0
    charlescount = 0
    dianacount = 0
    raymoncount = 0
   
    for row in csvreader:
        votecount = votecount +1
        if row[2] == "Charles Casper Stockham":
                charlescount = charlescount +1
        elif row[2] == "Diana DeGette":
                dianacount = dianacount +1
        else:
                raymoncount = raymoncount +1
    
    
    
    #find winner
    winner = max(raymoncount,dianacount,charlescount)
    
    #vote percents
    charpercent = charlescount/votecount
    dianapercent = dianacount/votecount
    raypercent = raymoncount/votecount
    
    #format percents
    charpercent = f"{charpercent:.0%}"
    dianapercent = f"{dianapercent:.0%}"
    raypercent = f"{raypercent:.0%}"
    
    #print results
output = (
            f'Election Results\n\n'
            f'------------------------------\n\n'
            f'Total Votes: {votecount}\n\n'
            f'------------------------------\n\n'
            f'Charles Casper Stockham: {charpercent} ({charlescount})\n'
            f'Diana DeGette: {dianapercent} ({dianacount})\n'
            f'Raymon Anthony Doane: {raypercent} ({raymoncount})\n\n'
            f'------------------------------\n\n'
            f'Winner: Diana DeGette \n\n'
            f'------------------------------'
         )
        
print(output)

with open('outputfile_pypoll.txt','w') as outfile:
    outfile.write(output)
