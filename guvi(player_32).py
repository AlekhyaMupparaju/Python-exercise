n=int(raw_input())
k=int(raw_input())
a=[]
fact=0
for i in range(n):
    b=int(raw_input())
    a.append(b)
for i in range(n):
    if k==a[i]:
        fact=1
if fact==1:
    print "YES"
else:
    print "NO"

    
