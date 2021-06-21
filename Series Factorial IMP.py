import math
def fact_sum(x,n):
    ff=0
    for i in range(1,n+1):
        ff+=((x**i)/math.factorial(i+1))
        ans=ff+1
    return round(ans,2)
print(fact_sum(5,4))
