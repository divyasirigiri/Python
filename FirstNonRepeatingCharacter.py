s1 = input()
res={}
for i in s1:
    if i in res:
        res[i]+=1
    else:
        res[i]=1
for i in s1:
    if(res[i]==1):
        print(i)
        break