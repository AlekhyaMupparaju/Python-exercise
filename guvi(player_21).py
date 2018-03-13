x1=int(raw_input())
y1=int(raw_input())
x2=int(raw_input())
y2=int(raw_input())
x3=int(raw_input())
y3=int(raw_input())
if x1==0 and x2==0 and x3==0:
    print "YES"
elif y1==0 and y2==0 and y3==0:
    print "YES"
else:
    n=(y2-y1)/(x2-x1)
    d=(y3-y1)/(x3-x1)
    if n==d:
        print "YES"
    else:
        print "NO"
    
