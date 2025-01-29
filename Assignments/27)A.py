'''27. A) Say a box of cookies can hold 24 cookies, and a container can hold 75 boxes of
cookies. Write a program that prompts the user to enter the total number of cookies,
then outputs the number of boxes and the number of containers to ship the cookies.
Note that each box must contain the specified number of cookies, and each container
must contain the specified number of boxes. If the last box of cookies contains less
than the number of specified cookies, you can discard it and output the number of
leftover cookies. Similarly, if the last container contains less than the number of
specified boxes, you can discard it and output the number of leftover boxes. Take the
capacity of the box and container from the keyboard.'''

n=int(input('no of cookies :'))
m=int(input('capacity of box: '))
a=int(input('capacity of container: '))
if(n<m):
    print('not sufficient')
else:
    c=n%m
    p=n//m
    print('extra cookies :',c)
    print('no of box  :',n//m)
if(p<a):
    print('not suff box')
else:
    d=p%a
    q=p//a
    print('no of container  :',q)
    print('extra box :',d)