# Display the marks of two students for 5 subjects using suitable graphical tools.
import matplotlib.pyplot as plt
import numpy as np
student={}
n=int(input("no of sub : "))
def student_dic(student):             # create dictionary for student data
    
    for i in range(n):
        key=input("Name of subject: ")
        value=int(input("Marks : "))
        student[key]=value
    return student
student1={}
student2={}
print("Data entry for 1st student")
print("student1 data : ",student_dic(student1))
print("Data entry for 2nd student")
print("student2 data : ",student_dic(student2))

m=student1.values()
n=student2.values()
plt(m)
plt(n)
plt.show()



