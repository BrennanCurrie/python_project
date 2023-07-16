#importing modules needed
import csv

# define file path
csvpath = '/Users/brennancurrie/Desktop/My_Code/Class_Materials/Challenges/Brennan_Currie_Module_3_Challenge/python_challenge/PyBank/Resources/budget_data.csv'

#open csv
with open(csvpath) as csvfile:

    #read csv/specify delimiter
    csvreader = csv.reader(csvfile, delimiter=',')
    
    
    #read the header first row
    csvheader = next(csvreader)
    
    
    #read each row after header
    monthcount = 0
    total = 0
    diff = 0
    increase = 0
    decrease = 0
    profitloss = 0
    prevprofitloss = 1088983
    totalchange = 0
    
    for row in csvreader:
        monthcount = monthcount +1
        total = total + int(row[1])
        profitloss = int(row[1])
        
        change = profitloss - prevprofitloss
        
        if change > increase:
            increase = change
            increasedate = row[0]
            
        if change < decrease:
            decrease = change
            decreasedate = row[0]
        #change = profitloss - prevprofitloss
        prevprofitloss = profitloss
        totalchange = change + totalchange
        
avg = total/monthcount

avgchange = totalchange/(monthcount-1)

#printing results
output = (
            f'Financial Analysis\n'
            f'------------------------------------------\n\n'
            f'Total Months: {monthcount}\n'
            f'Total: ${total}\n'
            f'Average Change: ${avgchange:.2f}\n'
            f'Greatest Increase in Profits: {increasedate} (${increase})\n'
            f'Greatest Decrease in Profits: {decreasedate} (${decrease})\n'
         )

print(output)
with open('outputfile_pybank.txt','w') as outfile:
   outfile.write(output)
