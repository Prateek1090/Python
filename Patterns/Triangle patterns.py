1
12
123
1234
'''n=int(input(":"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    print()'''


1
23
345
4567

'''n=int(input(":"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end="")
        i+=1
    print()'''

1
23
456
78910

n=int(input(":"))
x=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(x,end="")
        x=x+1
    print()