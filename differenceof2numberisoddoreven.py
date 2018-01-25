n=int(raw_input())
m=int(raw_input())
if n>m:
    c=n-m
else:
    c=m-n
if c%2==0:
    print "even"
else:
    print "odd"
