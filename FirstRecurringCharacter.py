s1 = input()
res ={}
flag=0
for i in s1:
    if i in res:
        res[i]+=1 
    else:
        res[i]=1 
for i in s1:
    if(res[i]>1):
        flag=1
        print(i)
        break
if flag==0:
    print("No recurring chars")
    
