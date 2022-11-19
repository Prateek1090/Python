'''
A B C D
A B C D
A B C D
A B C D

n=int(input(":"))
for i in range(1,n+1):
    for j in range(1,5):
        x=chr(ord('A')+j-1)
        print(x,end=" ")
    print()
'''

'''
A B C D 
B C D E 
C D E F 
D E F G 

n=int(input(":"))
for i in range(1,n+1):
    m=i
    for j in range(1,5):
        x = chr(ord('A') + m - 1)
        print(x,end=" ")
        m=m+1
    print()
'''

'''
A 
B C 
C D E 
D E F G 

n=int(input(":"))
for i in range(1,n+1):
    m=i
    for j in range(1,i+1):
        x = chr(ord('A') + m - 1)
        print(x,end=" ")
        m=m+1
    print()
'''


'''
E 
D E 
C D E 
B C D E 
A B C D E 

n=int(input(":"))
z=1
for i in range(1,n+1):
    a=1
    for j in range(1,i+1):
        x = (ord('A') + n - z)
        print(chr(x+a-1),end=" ")
        a=a+1
    print()
    z=z+1
'''
