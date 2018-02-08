n=int(raw_input())
k=int(raw_input())
a=[]
fct=0
for i in range(n):
    b=int(raw_input())
    a.append(b)
for i in range(n):
    if k==a[i]:
        fct=1
if fct==1:
    print "Yes"
else:
    print "No"
