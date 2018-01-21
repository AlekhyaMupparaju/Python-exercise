n=int(raw_input())
a=[]
for i in range(n):
    b=int(raw_input())
    a.append(b)
a.sort()
print a[0],a[n-1]
