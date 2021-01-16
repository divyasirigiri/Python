"""Write a program to find the numbers with unique digits in a range of given numbers"""
first,last = map(int,input().split(","))
print(first,last)
res=[]
for i in range(first,last):
    s = set(list(str(i)))
    if len(s) == len(list(str(i))):
        res.append(i)
print(res)
#input: 10,20
