'''B) Store 5 students marks for 6 subjects(randomly) then increments 5 marks for each
student for each subject then return Final Marks.'''

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

def final_marks(s):
    # Adding 5 to each value in the dictionary
    for key in s:
        s[key] += 5
    return s

fm1 = final_marks(a)
fm2 = final_marks(b)
fm3 = final_marks(c)
fm4 = final_marks(d)
fm5 = final_marks(e)

print(f'Final Marks for Student 1: {fm1}')
print(f'Final Marks for Student 2: {fm2}')
print(f'Final Marks for Student 3: {fm3}')
print(f'Final Marks for Student 4: {fm4}')
print(f'Final Marks for Student 5: {fm5}')
    