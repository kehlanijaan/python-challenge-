import os 
import csv

with open ('v.csv', 'w') as csvfile: 
    cwriter = csv.writer(csvfile, delimiter=',')
 
totalmonths = 0 
total = 0 
change = ()
profitlosses = ()
month = ()

csvpath = os.path.join ('budget_data.csv') 
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)


    for csvrow in csvreader:

    #Number of lines present
        totalmonths+=1
        #print(totalmonths)

    #Profitlosses Net total 
        total+=int(csvrow[1])
        #print(total)

    #Append Row Column to new list
        profitlosses.append(int(csvrow[1])) 

    #Calculate the profit and loss differences 
        change.append(profitloss[totalmonths-1]-profitloss[totalmonths-2])
        # print(profitloss)

    #Sum the difference
    totalchange = sum(change)

    #Calculate the average and dived by the total  rows **round to the second decimal place**
    averagechange = round(totalchange/(len(change)-1), 2)
    #print(averagechange)

    #Greatest increase in profit
    inc_profit = max(change)
    grt_increase = change.index(inc_profit)
  
    
    #Greatest decrease in profit
    dec_profit = min(change)
    grt_decrease = change.index(dec_profit)
  
    
print("Financial Analysis\n")
print("----------------------------\n")
print(f"Total Months: {totalmonths}\n")
print(f"Total: ${total} \n")
print(f"Average Change: ${averagechange}\n")
print(f"Greatest Increase in Profits: {month[grt_increase]} (${inc_profit}) \n")
print(f"Dreatest Decrease in Profits: {month[grt_decrease]} (${ dec_profit})\n")

close()








