import os
import csv

#Identify variables and store information
total_months=0
total_pl=0
value=[]
change=[]
dates=[]
profits=[]
g_date = None
g_value = 0
l_date = None
l_value = 0

#Read the first row
total_months+=1

path=os.path.join('Budget_Data.csv')
with open(path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',' )
    
    #Skip the header
    csvhead = next(csvreader)
    first_row=next(csvreader)
    #total_pl.append(first_row[1])
    #value.append(first_row[1])
    #Loop through the data and acquire information for lists
    for row in csvreader:
        #dates.append(row[0])
        dt = row[0]
        value = int(row[1])

        total_pl += value
        total_months += 1

        if value < l_value:
            l_value = value
            l_date = dt
        if value > g_value:
            g_value = value
            g_date = dt
        #Monthly changes
        #change.append(row[1]-value)
        #profits.append(change)
        

    #Average change
    avg_change=total_pl/total_months

    #Highest profit
    #greatest_increase=max(profits)
    #greatest_index=profits.index(greatest_increase)
    #greatest_date=dates[greatest_index]

    #Biggest decrease
    #greatest_decrease=min(profits)
    #lowest_index=profits.index(greatest_decrease)
    #lowest_date=dates[lowest_index]

#print the end results to the terminal
print('Financial Analysis')
print('------------------')
print(f'Total Months:{str(total_months)}')
print(f'Total:${str(total_pl)}')
print(f'Average Change:${str(round(avg_change,2))}')
print(f'Greatest Increase in Profits:{g_date} (${str(g_value)})')
print(f'greatest_decrease in Profits:{l_date} (${str(l_value)})')

#Set place for export
output_file=os.path.join("Financial_Analysis_Summary.txt")
with open(output_file,"w")as file:


#Then write to the file
    output=open('output.txt','w')

#Financial Analysis
    Line1='Financial Analysis'
    Line2='-----------------'
    Line3=str(f'Total Months:', total_months)
    Line4=str(f'Total:${str(total_pl)}')
    Line5=str(f'Average Change:${str(round(avg_change,2))}')
    line6=str(f'Greatest Increase in Profits:{g_date} (${str(g_value)})')
    Line7=str(f'Greatest Decrease in Profits:{l_date} (${str(l_value)})')