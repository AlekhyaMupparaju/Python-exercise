m=int(raw_input())
c=0
if m>1:
    for i in range(2,m):
        if m%i==0:
            c=c+1
if c>1:
   print "Yes"
else:
    print "No"
