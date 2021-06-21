'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
s = input()
res={}
max1=1
result=""

for i in s:
    if i in res:
        res[i]+=1 
    else:
        res[i] = 1 
for i in s:
    if res[i]>max1:
        max1=res[i]
        result = i
    else:
        pass
if result=="":
    print("No recurring char")
else:
    print("the most recurring char is ",result)