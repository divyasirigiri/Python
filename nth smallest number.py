ip=list(map(int,input().split()))
key = int(input('enter the n th smallest digit required'))
ip = sorted(ip)
print(ip[key-1])
