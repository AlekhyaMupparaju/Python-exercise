n=int(raw_input())
k=int(raw_input())
a=[]
count=0
for i in range(n):
    b=int(raw_input())
    a.append(b)
for i in range(n):
    if k==a[i]:
        count=count+1
print count
