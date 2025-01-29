# A store charges Rs.120 per item if you buy less than 10 items. If you buy
#between10 and 99 items, the cost is Rs.100 per item. If you buy100 or more items,
#the cost is Rs.70 per item. Write a program that asks the user how many items they
#are buying and prints the total cost.

n=int(input("no of elems :"))
if(n<10):
    print('Total cost :',n*120)
elif(n>=10 and n<99):
    print('Total cost :',n*100)
else:
    print('Total cost :',n*70)    
    