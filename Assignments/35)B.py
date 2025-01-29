'''B) Store 5 students marks for 6 subjects(randomly) and return average marks of each subject
and topper student.'''
stud={}
def student(stud):
    n=int(input('range:'))
    for i in range(n):
        key=input('Sub:')
        value=int(input('Marks :'))
        stud[key]=value
    return stud
student1={}
student2={}
student3={}
student4={}
student5={}
a=student(student1)
b=student(student2)
c=student(student3)
d=student(student4)
e=student(student5)
print(f'st1: {a}\nst2: {b}\n st3 : {c}\n st4 : {d}\nst5 :{e}')

def avg(li):
    s = sum(li.values())
    p = s / len(li)
    return p

av1 = avg(a)
av2 = avg(b)
av3 = avg(c)
av4 = avg(d)
av5 = avg(e)
print(f'av1: {av1}\nav2 :{av2}\nav3 ;{av3}\nav4 :{av4}\nav5 :{av5}')
avg_list=[av1,av2,av3,av4,av5]
print('topper :',max(avg_list))

        
    
        
        