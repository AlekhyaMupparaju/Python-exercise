n=int(raw_input())
k=int(raw_input())
a=[]
count=0
for i in range(n):
    b=int(raw_input())
    a.append(b)
a.sort()
for j in range(n):
    if a[j]%2!=0:
        count=count+1
        if k==count:
            print a[j]
