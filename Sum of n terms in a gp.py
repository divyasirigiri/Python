second = double(input('Enter Second: '))
third = double(input('Enter first: '))
r = third/second
n = int(input('Enter the nth term: '))
first = second/r
res = first
s = first
print("first",first)
for i in range(n-1):
    
    res = res*r
    print("-->",res)
    s = s + res
print(s)
