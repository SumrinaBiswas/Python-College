'''B) Read a text file which contain monthly electricity bills of different customers.
print the electricity consumption for July and November month.'''

#f=open('28)B.txt','r')

with open('28)B.txt','r') as f:
    c=f.readlines()
print(f'{c[1]} : {c[7]}\n{c[11]}')